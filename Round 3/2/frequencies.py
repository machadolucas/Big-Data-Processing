import nltk
import pandas as pd
import matplotlib.pyplot as plt

# Read the file data as a list of the 25 documents, removing the blank lines
with open('wikitexts.txt', encoding='utf-8') as f:
    documents = f.readlines()

documents = [x.strip() for x in documents if x != '\n']

# Tokenize documents into lists of words, and filter for only those words that have length >= 4
documents = [nltk.word_tokenize(x) for x in documents]
documents = [[x for x in doc if len(x) >= 4] for doc in documents]

# Create 'texts' objects with documents and a collection object
texts = [nltk.Text(x) for x in documents]
collection = nltk.text.TextCollection(texts)

# Get frequency distribution of words and convert to a dataframe with the words and 𝚝𝚏(w,D) (count or frequency)
distribution = nltk.FreqDist(collection)
df = pd.DataFrame(list(distribution.items()), columns=['word', 'count'])

# For each of the 25 texts, calculate tf_idf for all the words, and add results as columns to dataframe.
for i, text in enumerate(texts):
    df['tfidf_' + str(i + 1)] = df.apply(lambda row: collection.tf_idf(row['word'], text), axis=1)

# Sort by words alphabetically.
df = df.sort_values('word')

# Write output file
df.to_csv('frequencies.txt', sep=' ', encoding='utf-8', index=False, header=False)

# Sort by 𝚝𝚏(w,D) (frequency of words)
df = df.sort_values('count', ascending=False)

# Plot and save figure
plt.plot(list(range(0, len(df))), df['count'], linewidth=3, zorder=100)
plt.ylim(0, 65)
plt.xlim(0, 2200)
plt.savefig('frequencies.png')

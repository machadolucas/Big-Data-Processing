import pandas as pd
from scipy.spatial.distance import squareform, pdist

# Loads the data, dropping user identifier column (we use the indexes). Open the output file to write.
data = pd.read_csv('lastfm-matrix-germany.csv').drop('user', 1)
output = open('collfilter.txt', 'w')

# Compute an n-by-n table whose value artdists[x, y] contains the distance between artists in columns x and y.
# Transform to DataFrame since it is easier to manipulate and sort.
artdists = squareform(pdist(data.T, 'cosine'), force='tomatrix')
artdists_df = pd.DataFrame(artdists, columns=data.columns, index=data.columns)

# Iterate artists matrix to find maximum similarity. As several values are '1', it gets the first perfect match.
max_value = 0
max_item = ''
max_column = ''
for column in artdists_df.columns:
    value = artdists_df[column].max()
    if value > max_value:
        max_value = value
        max_column = column
        max_item = artdists_df[column].idxmax()

# Print into the file colfilter.txt a line that tells which two artists are most similar with each other.
# This should be in the form distance;artistA;artistB
output.write(str(max_value) + ';' + max_column + ';' + max_item + '\n')

# Compute an m-by-m table whose value usrdists[i, j] contains the distance between users i and j.
# Transform to DataFrame since it is easier to manipulate and sort.
usrdists = squareform(pdist(data, 'cosine'))
usrdists_df = pd.DataFrame(usrdists, columns=data.index, index=data.index)

# Iterate users matrix to find maximum similarity. As several values are '1', it gets the first perfect match.
max_value = 0
max_item = ''
max_column = ''
for column in usrdists_df.columns:
    value = usrdists_df[column].max()
    if value > max_value:
        max_value = value
        max_column = column
        max_item = usrdists_df[column].idxmax()

# Print into the file colfilter.txt a line that tells which two users are most similar with each other.
# This should be in the form distance;i;j,
output.write(str(max_value) + ';' + str(max_column) + ';' + str(max_item) + '\n')

# Get 10 most similar artists to 'michael jackson' and write to file in format 'distance artist'.
mj_similar = artdists_df['michael jackson'].sort_values(ascending=False).head(10)
for index, row in mj_similar.iteritems():
    output.write(str(row) + ' ' + index + '\n')

output.close()


# Note:
# According to an e-mail replied by the teacher, "having several similarities of value '1' just means that the answer
#  is not unique; pick any two that are 100% similar."

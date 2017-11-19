import warnings
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.neighbors import NearestNeighbors

# Ignore deprecation warnings from sklearn
warnings.filterwarnings("ignore")

# Load training, test and answers data sets.
df_train = pd.read_csv('vertigo_train.txt', sep=' ', header=None)
df_test = pd.read_csv('vertigo_predict.txt', sep=' ', header=None)
df_answers = pd.read_csv('vertigo_answers.txt', sep=' ', header=None)

# Create a perceptron, and train it with training data set.
p = Perceptron()
p.fit(df_train[[1, 2, 3, 4, 5]].values, df_train[0].values)

# Calculate predictions from test data set. Compare with answers to check who accurate it was.
predictions = p.predict(df_test.values)
correct = len([p for p, a in zip(predictions, [v[0] for v in df_answers.values]) if p == a])

# Calculate percentage of correct predictions
perceptron_accuracy = correct / df_answers.index.size  # Here I got ~65.46%

# Do it again with Perceptron(n_iter=100)
p = Perceptron(n_iter=100)
p.fit(df_train[[1, 2, 3, 4, 5]].values, df_train[0].values)
predictions = p.predict(df_test.values)
correct = len([p for p, a in zip(predictions, [v[0] for v in df_answers.values]) if p == a])
perceptron_accuracy_n100 = correct / df_answers.index.size  # Here I got ~81.96%

# Then I fit the training data for looking for 1 nearest neighbor.
neigh = NearestNeighbors(metric='manhattan', n_neighbors=1)
neigh.fit(df_train[[1, 2, 3, 4, 5]].values)

# Calculate index of nearest neighbor from training data and get class from it
nbrs_points = [x[0] for x in neigh.kneighbors(df_test.values, return_distance=False)]
nbrs_classes = [df_train.iloc[x][0] for x in nbrs_points]

# Calculate percentage of correct predictions
correct = len([p for p, a in zip(nbrs_classes, [v[0] for v in df_answers.values]) if p == a])
nearest_neighbor_accuracy = correct / df_answers.index.size  # Here I got ~74.74%

# I assumed we should print results for perceptron with n_iter=100 (it was not specified in question).
print('Perceptron: ' + str(round(perceptron_accuracy_n100 * 100, 2)) + '% correct')
print('Nearest neighbor: ' + str(round(nearest_neighbor_accuracy * 100, 2)) + '% correct')

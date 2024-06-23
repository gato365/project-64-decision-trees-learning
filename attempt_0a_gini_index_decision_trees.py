import numpy as np

# Sample data: labels of elements in a set
labels = np.array(['No'  'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes'])

# Count the occurrences of each label in the dataset
unique_labels, label_counts = np.unique(labels, return_counts=True)

# Calculate the probabilities of each label
probabilities = label_counts / label_counts.sum()

# Calculate the Gini index as 1 minus the sum of the squares of the probabilities
gini_index = 1 - np.sum(probabilities**2)

# Print out the unique labels, their counts, and probabilities for educational insight
print("Labels:", unique_labels)
print("Counts of each label:", label_counts)
print("Probabilities of each label:", probabilities)
print("Gini Index of the dataset:", gini_index)
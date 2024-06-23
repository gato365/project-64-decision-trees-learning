



## Import Numpy and Pandas
import numpy as np
import pandas as pd


##-----------------------------------------------------------
## Step 1: Create a data frame with 10 values
## Create a data frame in which the GPA is the independent variable and the Status is the dependent variable there will be 10 values
## GPA will be whole numbers 3 - 1'2, 2 - 2's, 2 - 3's, 3 - 4's
## Statuss will be any gpa above 3 is yes, any gpa below 3 is no

status_1_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'No', 'No','Yes', 'Yes', 'Yes', 'Yes', 'Yes']
})



status_2_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'Yes', 'Yes','Yes', 'Yes', 'Yes', 'Yes', 'Yes']
})




status_3_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes']
})



##-----------------------------------------------------------



##-----------------------------------------------------------
## Step 2: Create a function to calculate Gini Index

def gini_index(group, label_column):
    if len(group) == 0:
        return 0
    counts = group[label_column].value_counts(normalize=True)
    gini = 1 - sum(counts**2)
    return gini
##-----------------------------------------------------------


##-----------------------------------------------------------
## Step 3: Create a function to calculate Gini Index
## Function to evaluate splits and calculate both Gini indices and weighted Gini index
def evaluate_splits(data, split_points, feature, label):
    results = []
    for point in split_points:
        ## Split the data into two groups based on the feature value
        one = data[data[feature] <= point]
        two = data[data[feature] > point]
        
        ## Calculate Gini index for each group
        gini_one = gini_index(one, label)
        gini_two = gini_index(two, label)
        
        ## Calculate weighted Gini index for the split
        total = len(data)
        weight_one = len(one) / total
        weight_two = len(two) / total
        weighted_gini = (weight_one * gini_one) + (weight_two * gini_two)
        
        ## Store results
        results.append({
            'split_point': point,
            'gini_one': gini_one,
            'gini_two': gini_two,
            'weighted_gini': weighted_gini
        })
    return results
##-----------------------------------------------------------








## Specified split points for df 1
split_1_points = status_1_df['GPA'].unique().tolist()

## Calculate Gini indices for the splits for df 1
split_1_results = evaluate_splits(status_1_df, split_1_points, 'GPA', 'Status')

## Display the results for df 1
print("Split 1 Results")
for result in split_1_results:
    print(f"Split at {result['split_point']}: Gini One = {result['gini_one']:.4f}, "
          f"Gini Two = {result['gini_two']:.4f}, Weighted Gini = {result['weighted_gini']:.4f}")




## Specified split points for df 2
split_2_points = status_2_df['GPA'].unique().tolist()


## Calculate Gini indices for the splits for df 2
split_2_results = evaluate_splits(status_2_df, split_2_points, 'GPA', 'Status')


## Display the results for df 2
print("\nSplit 2 Results")
for result in split_2_results:
    print(f"Split at {result['split_point']}: Gini One = {result['gini_one']:.4f}, "
          f"Gini Two = {result['gini_two']:.4f}, Weighted Gini = {result['weighted_gini']:.4f}")



## Specified split points for df 3
split_3_points = status_3_df['GPA'].unique().tolist()

## Calculate Gini indices for the splits for df 3
split_3_results = evaluate_splits(status_3_df, split_3_points, 'GPA', 'Status')


## Display the results for df 3
print("\nSplit 3 Results")
for result in split_3_results:
    print(f"Split at {result['split_point']}: Gini One = {result['gini_one']:.4f}, "
          f"Gini Two = {result['gini_two']:.4f}, Weighted Gini = {result['weighted_gini']:.4f}")

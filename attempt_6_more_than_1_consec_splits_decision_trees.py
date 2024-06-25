
## Import Numpy and Pandas
import numpy as np
import pandas as pd
from random import randrange

##-----------------------------------------------------------
## Step 1: Create a data frame with 10 values
## Create a data frame in which the GPA is the independent variable and the Status is the dependent variable there will be 10 values


status_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'Yes', 'Yes','No', 'No', 'Yes', 'Yes', 'Yes']
})

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

## Specified split points
## WHy can't we just use the unique values in the GPA column?
## We can use the unique values in the GPA column but it will not give us the desired result

split_points = status_df['GPA'].unique().tolist()


## Calculate Gini indices for the splits
split_results = evaluate_splits(status_df, split_points, 'GPA', 'Status')





# Step 4: Perform further splits within each group after finding the minimum Gini index

def perform_further_splits(data, feature, label):
    # Calculate initial split points
    split_points = data[feature].unique().tolist()
    split_results = evaluate_splits(data, split_points, feature, label)
    
    # Find the split with the minimum weighted Gini index
    min_gini_result = min(split_results, key=lambda x: x['weighted_gini'])
    print(f"Minimum Gini Split: {min_gini_result}")
    
    # Perform further splits within each group formed by the minimum Gini split
    split_point = min_gini_result['split_point']
    group_one = data[data[feature] <= split_point]
    group_two = data[data[feature] > split_point]
    
    if not group_one.empty:
        print("Further splitting Group One")
        split_points_one = group_one[feature].unique().tolist()
        split_results_one = evaluate_splits(group_one, split_points_one, feature, label)
        for result in split_results_one:
            print(f"Group One Split at {result['split_point']}: Weighted Gini = {result['weighted_gini']:.4f}")
    
    if not group_two.empty:
        print("Further splitting Group Two")
        split_points_two = group_two[feature].unique().tolist()
        split_results_two = evaluate_splits(group_two, split_points_two, feature, label)
        for result in split_results_two:
            print(f"Group Two Split at {result['split_point']}: Weighted Gini = {result['weighted_gini']:.4f}")


# Function to create a pseudo decision tree based on further splits

def create_pseudo_tree(data, feature, label, depth=0, max_depth=3):
    if depth < max_depth:
        # Calculate initial split points
        split_points = data[feature].unique().tolist()
        split_results = evaluate_splits(data, split_points, feature, label)
        
        # Find the split with the minimum weighted Gini index
        if split_results:  # Ensure there are split results to process
            min_gini_result = min(split_results, key=lambda x: x['weighted_gini'])
            split_point = min_gini_result['split_point']
            group_one = data[data[feature] <= split_point]
            group_two = data[data[feature] > split_point]
            
            print(f"{'  '*depth}Split at {split_point}: Weighted Gini = {min_gini_result['weighted_gini']:.4f}")
            
            # Recursively split each group further
            if not group_one.empty:
                print(f"{'  '*depth}Further splitting Group One")
                create_pseudo_tree(group_one, feature, label, depth+1, max_depth)
            
            if not group_two.empty:
                print(f"{'  '*depth}Further splitting Group Two")
                create_pseudo_tree(group_two, feature, label, depth+1, max_depth)
        else:
            print(f"{'  '*depth}No further splits possible.")
    else:
        print(f"{'  '*depth}Maximum depth reached.")


## Display the results
for result in split_results:
    print(f"Split at {result['split_point']}: Gini One = {result['gini_one']:.4f}, "
          f"Gini Two = {result['gini_two']:.4f}, Weighted Gini = {result['weighted_gini']:.4f}")
    


perform_further_splits(status_df, 'GPA', 'Status')
create_pseudo_tree(status_df, 'GPA', 'Status', max_depth=3)
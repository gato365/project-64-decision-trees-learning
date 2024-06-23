



## Import Numpy and Pandas
import numpy as np
import pandas as pd


##-----------------------------------------------------------
## Step 1: Create a data frame with 10 values
## Create a data frame in which the GPA is the independent variable and the Status is the dependent variable there will be 10 values
## GPA will be whole numbers 3 - 1'2, 2 - 2's, 2 - 3's, 3 - 4's
## Statuss will be any gpa above 3 is yes, any gpa below 3 is no

status_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'No', 'No','Yes', 'Yes', 'Yes', 'Yes', 'Yes']
})

##-----------------------------------------------------------


##-----------------------------------------------------------
## Step 2: Specify the algorithmic details

### Specify Variables:
#### Independent Variable: GPA 
#### Dependent Variable: Status

### Algorithm: Decision Tree 
#### Decision Tree Type: Classification within CART (Classification and Regression Trees)
#### Splitting Criterion: Gini Index
#### Maximum Depth: 2

##-----------------------------------------------------------




##-----------------------------------------------------------
## Step 3: Build the Decision Tree
### Step 3.1 - Splitting the DataFrame based on the condition GPA <= 3

group_1 = status_df[status_df['GPA'] <= 3]
group_2 = status_df[status_df['GPA'] > 3]



### Step 3.2 - Calculate the Gini Index for each group

def gini_index(group, classes):
    n_instances = float(len(group))
    if n_instances == 0:  # Avoid division by zero
        return 0
    score = 0.0
    # Sum the squared proportion of each class
    for class_val in classes:
        p = (group['Status'] == class_val).sum() / n_instances
        score += p * p
    return 1.0 - score



# List of unique class values
classes = status_df['Status'].unique()

# Calculate Gini Index for each group
gini_group_1 = gini_index(group_1, classes)
gini_group_2 = gini_index(group_2, classes)

print(f"Gini Index for Group 1 (GPA <= 3): {gini_group_1}")
print(f"Gini Index for Group 2 (GPA > 3): {gini_group_2}")


### Step 3.3 - Calculate the weighted Gini Index 

n_instances = float(len(status_df))
weighted_gini_1 = (len(group_1) / n_instances) * gini_group_1
weighted_gini_2 = (len(group_2) / n_instances) * gini_group_2

weighted_gini = weighted_gini_1 + weighted_gini_2


print(f"Weighted Gini Index: {weighted_gini}")
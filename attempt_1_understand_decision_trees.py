



## Import Numpy and Pandas
import numpy as np
import pandas as pd


## Create a data frame in which the GPA is the independent variable and the Status is the dependent variable there will be 10 values
## GPA will be whole numbers 3 - 1'2, 2 - 2's, 2 - 3's, 3 - 4's
## Statuss will be any gpa above 3 is yes, any gpa below 3 is no

np.random.seed(42)
status_df = pd.DataFrame({
    'GPA': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'Status': ['No', 'No', 'No', 'No', 'No','Yes', 'Yes', 'Yes', 'Yes', 'Yes']
})


print(status_df)
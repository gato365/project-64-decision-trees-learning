import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples
n_samples = 1000

# Generate GPA data between 0.0 and 4.0
gpas = np.random.uniform(low=0.0, high=4.0, size=n_samples)

# Generate student statuses based on GPA
# More simplistic rules for categorization:
# - GPA below 2.5 leads to 'Reject'
# - GPA between 2.5 and 3.5 leads to 'Waitlist'
# - GPA above 3.5 leads to 'Hire'
statuses = np.where(gpas < 2.5, 'Reject', np.where(gpas < 3.5, 'Waitlist', 'Hire'))

# Create a DataFrame
data = pd.DataFrame({
    'GPA': gpas,
    'Status': statuses
})

print(data.head())

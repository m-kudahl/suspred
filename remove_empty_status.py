import pandas as pd

# Read the CSV file
df = pd.read_csv('combined_data.csv')

# Remove rows with empty values in the specified columns
df.dropna(subset=['status'], inplace=True)

# Write the cleaned dataframe to a new CSV file
df.to_csv('cleaned_combined_data.csv', index=False)
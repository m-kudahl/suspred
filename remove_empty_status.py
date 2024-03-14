
import pandas as pd

# Read CSV files into DataFrames
file1_df = pd.read_csv('Filtered_No_Guac.csv')
file2_df = pd.read_csv('graduation.csv')

# Drop all columns from file2_df except 'name' and 'status'
file2_df = file2_df[['name', 'status']]

# Merge DataFrames based on the common column
merged_df = pd.merge(file1_df, file2_df, how='left', left_on='project', right_on='name')

# Update status column in file1_df with the values from file2_df
file1_df['status'] = merged_df['status']

# Remove rows with empty values in the specified columns
file1_df.dropna(subset=['status'], inplace=True)

# Write the cleaned dataframe to a new CSV file
file1_df.to_csv('cleaned_combined_data.csv', index=False)
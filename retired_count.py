import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Filtered_Data.csv")

# Count the number of rows where the 'status' column has 'retired' entry
retired_count = len(df[df['status'] == 'retired'])

print("Number of rows with 'retired' status:", retired_count)

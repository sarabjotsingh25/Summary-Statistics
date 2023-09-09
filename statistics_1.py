import pandas as pd
import statistics

# Load the dataset from the CSV file
df = pd.read_csv('data.csv')

# Calculate the mean
mean = df['values'].mean()

# Calculate the median
median = df['values'].median()

# Calculate the mode
mode = statistics.mode(df['values'])

# Calculate the standard deviation
std_dev = df['values'].std()

# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")

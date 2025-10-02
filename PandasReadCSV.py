# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Read CSV Files ----------

# A simple way to store big data sets is to use CSV files (comma separated files)
# A CSV contains plain text and is a well known format that can be read by everyone including Pandas
# In our examples we will be using a CSV file called "data.csv"

# Load the CSV into a DataFrame
df = pd.read_csv('data.csv')

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print the entire DataFrame

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows

# Divider
print(dLen)

# Print the DataFrame without the "to_string()" method
print(df)

# ---------- max_rows ----------

# The number of rows return is defined in Pandas option settings
# You can check your system's maximum rows with the "pd.options.display.max_rows" statement

print(pd.options.display.max_rows)

# Divider
print(dLen)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the "print(df)" statement
# will return only the headers and the first and last 5 rows

# You can change the maximum rows number with the same statement

# Increase the maximum number of rows to display the entire DataFrame
pd.options.display.max_rows = 9999

print(df)

# Divider
print(dLen)
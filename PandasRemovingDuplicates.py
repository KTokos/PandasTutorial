# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Discovering Duplicates ----------

# Duplicate rows are rows that have been registered more than one time

# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates

# To discover duplicates, we can use the "duplicated()" method

# The "duplicated()" method returns a boolean values for each row

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Returns True for every row that is a duplicate, otherwise False
print(df.duplicated().to_string())  # Use "to_string()" to print out entire DataFrame

# Divider
print(dLen)

# ---------- Removing Duplicates ----------

# To remove duplicates, use the "drop_duplicates()" method

# Remove all duplicates
df.drop_duplicates(inplace=True)

# REMEMBER: The (inplace=true) will make sure that the method does NOT return a new DataFrame, but it will remove
#           all duplicates from the original DataFrame

# Print out DataFrame
print(df.to_string())   # Use "to_string()" to print out entire DataFrame
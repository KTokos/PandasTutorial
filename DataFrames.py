# Divider length
import pandas

dLen = '-' * 20

# ---------- What is a DataFrame ----------

# A Pandas DataFrame is a 2-dimensional data structure, like a 2-dimensional array, or a table with rows and columns

# Create a simple Pandas DataFrame

# Imports
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Load data into a DataFrame object
df = pd.DataFrame(data)

# Print out DataFrame
print(df)

# Divider
print(dLen)

# ---------- Locate Row ----------

# Pandas uses the "loc" attribute to return one or more specified rows

# Refer to the row index, return row 0
print(df.loc[0])

# Return row 0 and 1 using a list of indexes
print(df.loc[[0, 1]]) # * NOTE DOUBLE BRACKETS *

# Divider
print(dLen)

# ---------- Named Indexes ----------

# With the index argument, you can name your own indexes

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Add a list of names to give each row a name
df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# Print out DataFrame
print(df)

# Divider
print(dLen)

# ---------- Locate Named Indexes ----------

# Use the named index in the "loc" attribute to return the specified row

# Return "day2", refer to the named index
print(df.loc["day2"])

# Divider
print(dLen)

# ---------- Load Files Into a DataFrame ----------

# If your datasets are stored in a file, Pandas can load them into a DataFrame

# Load a comma separated file (CSV) into a DataFrame
df = pd.read_csv('customers-100.csv')

print(df)
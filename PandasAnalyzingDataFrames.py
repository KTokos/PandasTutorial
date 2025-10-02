# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Viewing the Data ----------

# One of the most used methods for getting a quick overview of the DataFrame, is the "head()" method
# The "head()" method returns the headers and a specified number of rows, starting from the top

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Get a quick overview by printing the first 10 rows of the DataFrame
print(df.head(10))

# Note: If the number of rows is not specified, the "head()" method will return the top 5 rows

# Divider
print(dLen)

# Print first 5 rows
print(df.head())

# Divider
print(dLen)

# There is also a "tail()" method for viewing the last rows of the DataFrame
# The "tail()" method returns the headers and a specified number of rows, starting from the bottom

# Print the last 5 rows of the dataframe
print(df.tail())

# Divider
print(dLen)

# ---------- Info About the Data ----------

# The DataFrames object has a method called "info()", that gives you more information about the data set

# Print information about the data
print(df.info())

# The result tells us there are 169 rows and 4 columns
# and the name of each column, with the data type

# ---------- Null Values ----------

# The "info()" method also tells us how many Non-Null values there are present in each column, and in our data set
# it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values.
# This is a step towards what is called "cleaning data", and you will learn more about that in the next chapters

# Divider
print(dLen)
# Divider length
dLen = '-' * 20

# ---------- What is a Series ----------

# A pandas series is like a column in a table
# Imports
import pandas as pd

# One dimensional array holding data of any time
a = [1, 7, 2]

# Assign array to a series
myVar = pd.Series(a)

# Print out series
print(myVar)

# Divider
print(dLen)

# ---------- Labels ----------

# If nothing else is specified, the values are labeled with their index number

# Return the first value of the series
print(myVar[0])

# Divider
print(dLen)

# ---------- Create Labels ----------

# With the "index" argument, you can create your own labels
myVar = pd.Series(a, index=["x", "y", "z"])

# Print out series
print(myVar)

# Return the value of y
print(myVar["y"])

# Divider
print(dLen)

# ---------- Key/Value Objects as Series ----------

# You can also use a key/value object, like a dictionary, when creating a series

# Create a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}

# Turn the dictionary into a series
myVar = pd.Series(calories)

# Print out the series
print(myVar)

# Create a series using only data from "day1" and "day2"
myVar = pd.Series(calories, index=["day1", "day2"])

# Print out the series
print(myVar)

# Divider
print(dLen)

# ---------- DataFrames ----------

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames
# Series is like a column, a DataFrame is a whole table

# Create a DataFrame from two Series
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create a DataFrame
myVar = pd.DataFrame(data)

# Print out DataFrame
print(myVar)

# Divider
print(dLen)
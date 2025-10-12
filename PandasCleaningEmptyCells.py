# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Empty Cells ----------

# Empty cells can potentially give you a wrong result when you analyze data

# ---------- Remove Rows ----------

# One way to deal with empty cells is to remove rows that contain empty cells

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the reuslt

# Read CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Return a new DataFrame with no empty cells
new_df = df.dropna()

# Print out the new DataFrame
print(new_df.to_string())   # Use "to_string()" to print the entire DataFrame

# Divider
print(dLen)

# NOTE: By default, the "dropna()" method returns a new DataFrame, and will not change the original

# If you want to change the original DataFrame, use the inplace = True argument
# Remove all rows with NULL values
df.dropna(inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# Divider
print(dLen)

# NOTE: Now, the "dropna(inplace=True)" will NOT return a new DataFrame, but it will remove all rows containing NULL
#       values from the original DataFrame

# ---------- Replace Empty Values ----------

# Another way of dealing with empty cells is to insert a new value instead

# This way you do not have to delete entire rows just because of some empty cells

# The "fillna()" method allows us to replace empty cells with a value

# Reread CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Replace NULL values with the number 130
df.fillna(130, inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# Divider
print(dLen)

# ---------- Replace Only For Specified Columns ----------

# The example above replaces all empty cells in the whole DataFrame

# To only replace empty values for one column, specify the column name for the DataFrame

# Reread CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Replace NULL values in the "Calories" column with the number 130
df.fillna({"Calories": 130}, inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# Divider
print(dLen)

# ---------- Replace Using Mean, Median, or Mode ----------

# A common way to replace empty cells, is to calculate the mean, median or mode value of the column

# Pandas uses the "mean()", "median()" and "mode()" methods to calculate the respective values for a specified column

# --- Mean ---

# Reread CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Calculate the MEAN of the "Calories" column
x = df["Calories"].mean()

# Replace any empty values in the "Calories" column with the calculated MEAN
df.fillna({"Calories": x}, inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# Divider
print(dLen)

# NOTE: Mean = the average value (the sum of all values divided by number of values)

# --- Median ---

# Reread CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Calculate the MEDIAN of the "Calories" column
x = df["Calories"].median()

# Replace any empty values in the "Calories" column with the calculated MEDIAN
df.fillna({"Calories": x}, inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# NOTE: Median = the value in the middle, after you have sorted all values ascending

# --- Mode ---

# Reread CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Calculate the MODE of the "Calories" column
x = df["Calories"].mode()[0]

# Replace any empty values in the "Calories" column with the calculated Median
df.fillna({"Calories": x}, inplace=True)

# NOTE: Mode = the value that appears most frequently
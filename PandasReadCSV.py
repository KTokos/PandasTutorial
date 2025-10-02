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
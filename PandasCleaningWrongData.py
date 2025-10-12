# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Wrong Data ----------

# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered
# "199" instead of "1.99".

# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be

# If you take our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration
# is between 30 and 60

# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we
# could conclude with the fact that this person did not work out for 450 minutes

# How can we fix wrong values, like the one for "Duration" in row 7?

# ---------- Replacing Values ----------

# One way to fix wrong values is to replace them with something else

# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert
# "45" in row 7

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Set "Duration" in row 7 to 45
df.loc[7, 'Duration'] = 45

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets

# To replace wrong data for larger sets you can create some rules, e.g. set some boundaries for legal values, and
# replace any values that are outside the boundaries

# Loop through all values in the "Duration" column
for x in df.index:
    # If the value is higher than 120
    if df.loc[x, 'Duration'] > 120:
        # Set it to 120
        df.loc[x, 'Duration'] = 120

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out entire DataFrame

# ---------- Removing Rows ----------

# Another way of handling wrong data is to remove the rows that contains wrong data

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to
# do your analyses

# Loop through all values in the "Duration" column
for x in df.index:
    # If the value is higher than 120
    if df.loc[x, 'Duration'] > 120:
        # Delete the row
        df.drop(x, inplace=True)

# Print out the DataFrame
print(df.to_string())   # Use "to_string()" to print out the entire DataFrame

# Divider
print(dLen)
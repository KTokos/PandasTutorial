# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Read JSON ----------

# Big data sets are often stored, or extracted as JSON
# JSON is plain text, but has the format of an object, and is known in the world of programming, including Pandas
# In our examples we will be using a JSON file called 'data.json'

# Load the JSON file into a DataFrame
df = pd.read_json('data.json')

# Print out DataFrame
print(df.to_string())   # Use "to_string()" to print the entire DataFrame

# Divider
print(dLen)

# ---------- Dictionary as JSON ----------

# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly

# Load a Python Dictionary into a DataFrame
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Print out DataFrame
print(df)

# Divider
print(dLen)
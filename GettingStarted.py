# Import pandas
import pandas as pd

# Declare dataset
myDataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3, 7, 2]
}

# Assign dataset to a dataframe using pandas
myVar = pd.DataFrame(myDataset)

# Print out dataset
print(myVar)

# Print pandas version
#print(pd.__version__)
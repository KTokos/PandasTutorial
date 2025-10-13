# Imports
import pandas as pd

# Divider length
dLen = '-' * 20

# ---------- Finding Relationships ----------

# A great aspect of the Pandas module is the "corr()" method

# The "corr()" method calculates the relationship between each column in your data set

# The examples in this page uses a CSV file called: 'correlations.csv'

# Read CSV file into a DataFrame
df = pd.read_csv('correlations.csv')

# Show the relationship between the columns
print(df.corr())

# Divider
print(dLen)

# NOTE: The "corr()" method ignores "not numeric" columns

# ------ Result Explained ------

# The Result of the "corr()" method is a table with a lot of numbers that represents how well the relationship is
# between two columns

# The number varies from -1 to 1

# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up
# in the first column, the other one went up as well

# 0.9 is a good relationship, and if you increase one value, the other one will probably increase as well

# -0.9 would be just as good of a relationship as 0.9, but if you increase one value, the other one will probably go
# down

# 0.2 means NOT a good relationship, meaning that if one value goes up, the other one probably won't go up

# WHAT IS A GOOD CORRELATION: It depends on the use, but I think it is safe to say you have to have at least 0.6 (or
#                             -0.6) to call it a good correlation

# ----- Perfect Correlation -----

# We can see that "Duration" and "Duration" got the number '1.00000', which makes sense, each column always has a
# perfect relationship with itself

# ----- Good Correlation -----

# "Duration" and "Calories" got a '0.922717' correlation, which is a very good correlation, and we can predict that the
# longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you
# probably had a long work out

# ----- Bad Correlation -----

# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict
# the max pulse just by looking at the duration of the workout, and vice versa
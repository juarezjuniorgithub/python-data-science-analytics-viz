import pandas as pd

df = pd.read_csv("C:\\python-datasets\\data.csv")

# the number of rows is not specified the head() method will return the top 5 rows
# # print first 5 rows of the DataFrame
#print(df.head())

# print the first 10 rows of the DataFrame
#print(df.head(10))

# print last 5 rows of the DataFrame
#print(df.tail()) 

# print information about the data set
print(df.info())


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame, which is like a table with rows and columns
df = pd.DataFrame(data)

print(df)

#you can refer to the row index
print(df.loc[0])

#you can also use a list of indexes
#print(df.loc[[0, 1]])

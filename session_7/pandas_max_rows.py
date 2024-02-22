import pandas as pd

print(pd.options.display.max_rows) 

pd.options.display.max_rows = 9999

df = pd.read_csv("C:\\python-datasets\\data.csv")

print(df) 
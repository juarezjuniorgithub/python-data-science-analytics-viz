import pandas as pd

df = pd.read_json("C:\\python-datasets\\data.json")

print(df.to_string())
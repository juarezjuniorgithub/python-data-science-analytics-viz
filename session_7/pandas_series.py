import pandas as pd

my_dict = {'a': 1, 'b': 2, 'c': 3}

ser = pd.Series(data=my_dict, index=['a', 'b', 'c'])

print(ser)


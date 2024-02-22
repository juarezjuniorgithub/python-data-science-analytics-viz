# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html

import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
print(df)

new_df = df.fillna(0)
print(new_df)

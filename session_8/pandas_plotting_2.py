import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\python-datasets\\data.csv")

# scatter plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
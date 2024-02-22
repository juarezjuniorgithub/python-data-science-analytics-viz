import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\python-datasets\\data.csv")

# a histogram needs only one column
# a histogram shows us the frequency of each interval - how many workouts lasted between 50 and 60 minutes?
# use the "Duration" column to create the histogram
# it will tell us that there were over 100 workouts that lasted between 50 and 60 minutes
df["Duration"].plot(kind = 'hist')

plt.show()
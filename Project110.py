import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].to_list()

population_mean = statistics.mean(data)

print("Population mean of this data is: ", population_mean)

# population_std = statistics.stdev(data)
# print("Standard Deviation of this data is: ", population_std)

data_set = []
for i in range(0, 1000):
    random_index = random.randint(0, len(data)-1)
    value = data[random_index]
    data_set.append(value)
mean = statistics.mean(data_set)
std = statistics.stdev(data_set)
print("Sampling mean of this data is: ", mean)


fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()

# from prettytable import from_csv
import numpy as np
import pandas as pd

# with open("game_data.csv", "r") as fp:
#     datatable = from_csv(fp)
# print(type(datatable

datatable = pd.read_csv('game_data.csv')
for col in datatable.columns:
    print(col)

unique_set = np.unique(datatable["Speed_set"])

gk = datatable.groupby("Side")["Speed_set", "Status"].value_counts()

print(gk)


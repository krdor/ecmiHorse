import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# with open("game_data.csv", "r") as fp:
#     datatable = from_csv(fp)
# print(type(datatable))

datatable = pd.read_csv('game_data.csv')
# print(datatable.to_string())

whites = datatable[datatable['Side'] == "W"]
blacks = datatable[datatable['Side'] == "B"]

# print(whites.to_string(), "\n", blacks.to_string())
games_wins_w = []
games_wins_b = []
for i in range(1, 6):
    setW = whites[whites['Speed_set'] == i]
    games = setW.shape[0]
    wins = setW[setW["Status"] == 1].shape[0]
    games_wins_w.append(([i, (wins / games)]))

    setB = blacks[blacks['Speed_set'] == i]
    games = setB.shape[0]
    wins = setB[setB["Status"] == 1].shape[0]
    games_wins_b.append([i, (wins / games)])

winning_df_black = pd.DataFrame(games_wins_b, columns=['Set Number', 'Win Percentage'])

winning_df_white = pd.DataFrame(games_wins_w, columns=['Set Number', 'Win Percentage'])

print(winning_df_black, "\n", winning_df_white)

# Data about Female and Male
female = datatable[datatable['Gender'] == "F"]
male = datatable[datatable['Gender'] == "M"]

print(female, male)

# count_female_win = female[female["Status"]== 1].shape[0]    counting of winning women
# count_male_win = male[male["Status"]== 1].shape[0]          counting of winning women

# print(datatable.groupby('Gender')['Status'].count())

# female_win_data = female[female['Status'] != 0].reset_index()
# male_win_data = male[male['Status'] != 0].reset_index()

# res_female_df = female_win_data.groupby['Gender'.count()
# res_female_df = female_win_data['Status', 'Gender']

# print(female, male)


# # Graph Playing White
# _ , axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
# axes = axes.flatten()

# color_rectangle = np.random.rand(7, 3)


# axes[0].bar(winning_df_white['Set Number'], winning_df_white["Win Percentage"], color=color_rectangle, align='center')
# axes[0].set(xlabel='Number of the set', ylabel='Winning Percentage(%)', title='Influence of playing for "White" ')
# axes[0].yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

# axes[0].grid()

# # Graph Playing Black
# axes[1].bar(winning_df_black['Set Number'], winning_df_black["Win Percentage"], color=color_rectangle, align='center')
# axes[1].set(xlabel='Number of the set', ylabel='Winning Percentage(%)', title='Influence of playing for "Black"')
# axes[1].grid()

# axes[1].yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

# plt.tight_layout()
# plt.show()
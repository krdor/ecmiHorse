import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# with open("game_data.csv", "r") as fp:
#     datatable = from_csv(fp)
# print(type(datatable))

datatable = pd.read_csv('game_data.csv')


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

female_win = female[female['Status'] == 1].shape[0]
female_lose = female[female['Status'] == 0].shape[0]

male_win = male[male['Status'] == 1].shape[0]
male_lose = male[male['Status'] == 0].shape[0]

# Graph that introduces the statistics of Winning and Losing between Male and Female
graph_data = [female_win, female_lose, male_win, male_lose]
labels = ['Female Win', 'Female Lose', 'Male Win ', 'Male Lose']

#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
#explsion
explode = (0.05, 0.05, 0.05, 0.05)
_, ax = plt.subplots()
ax.axis('equal') 
 
plt.pie(graph_data, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)

#draw circle
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Win/Lose contribution by Gender') 
plt.savefig("Win Lose contribution by Gender.png")
plt.tight_layout()
plt.show()


# Graph Playing White
_ , axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes = axes.flatten()

# color_rectangle = np.random.rand(7, 3)
colorss = ['#003f5c','#58508d','#bc5090','#ff6361', '#ffa600' ]
axes[0].set_axisbelow(True)
axes[0].grid(alpha = 0.5)
axes[0].bar(winning_df_white['Set Number'], winning_df_white["Win Percentage"], color= colorss, align='center')
axes[0].set(xlabel='Number of the set', ylabel='Winning Percentage(%)', title='Influence of playing for "White" ')
axes[0].yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))




# Graph Playing Black
axes[1].set_axisbelow(True)
axes[1].grid(alpha = 0.5)
axes[1].bar(winning_df_black['Set Number'], winning_df_black["Win Percentage"], color=colorss, align='center')
axes[1].set(xlabel='Number of the set', ylabel='Winning Percentage(%)', title='Influence of playing for "Black"')
axes[1].yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

plt.savefig("Graph Playing White and Black.png")
plt.tight_layout()
plt.show()

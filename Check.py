import pandas as pd

datatable = pd.read_csv('game_data.csv')

whites = datatable[datatable['Side'] == "W"]
blacks = datatable[datatable['Side'] == "B"]

games_wins_w = []
games_wins_b = []
for i in range(1, 6):
    setW = whites[whites['Speed_set'] == i]
    games = setW.shape[0]
    wins = setW[setW["Status"] == 1].shape[0]
    games_wins_w.append(([i, (wins, games)]))

    setB = blacks[blacks['Speed_set'] == i]
    games = setB.shape[0]
    wins = setB[setB["Status"] == 1].shape[0]
    games_wins_b.append([i, (wins, games)])

winning_df_black = pd.DataFrame(games_wins_b, columns=['Set Number', 'Win Percentage'])

winning_df_white = pd.DataFrame(games_wins_w, columns=['Set Number', 'Win Percentage'])

print("-------------------White sets--------------------\n", winning_df_white,
      "\n---------------------Black Sets------------------\n", winning_df_black)
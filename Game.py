import random as rand


def white_win_prob(N):  # We can compute values for n - 1 numbers at the start and keep it in an array to optimize code
    if N == 1:
        return 1
    else:
        return (1 / N) + ((N - 1) / N) * ((0.5 ** (1 / (N - 1))) - ((1 - white_win_prob(N - 1)) ** (N / (N - 1))))


def single_round(maximum_round, race_number, pc, oc):
    i = maximum_round - race_number
    speed = rand.random()
    print(f"The average speed in the round {race_number + 1} was {speed}")
    if pc == -1:
        print("Do you want to claim this round?")
        player_flag = str(input("Y/N: "))
        if player_flag == 'Y':
            pc = speed
            player_flag = 1
        if player_flag == 0 and oc == -1 and i != 2 and speed >= (1 - white_win_prob(i - 1)) ** (1 / (i - 1)):
            oc = speed
        elif player_flag == 0 and oc == -1 and i == 2:
            oc = speed
    elif pc != -1 and oc == -1:
        if i == 1:
            oc = speed
            print("Computer chose this value.")
        else:
            if speed > pc:
                oc = speed
                print("Computer chose this value.")
    return pc, oc


print("Hello, welcome to the:\nH O R S E    G  A M E\nYour objective is to bet a higher randomly generated number "
      "than your opponent, which is the computer.\n")

number_of_races = int(input("Choose the amount of generated numbers: "))
player_choice = -1
opponent_choice = -1

for r in range(number_of_races):
    player_choice, opponent_choice = single_round(number_of_races, r, player_choice, opponent_choice)

winner = "null"
if player_choice > opponent_choice:
    winner = "Y O U   W O N !!!"
else:
    winner = "Computer won :]"
print(f"\nYour score: {player_choice}\nComputer score: {opponent_choice}")
print(f"\n{winner}")

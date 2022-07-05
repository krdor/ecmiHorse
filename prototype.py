import random as rand
import numpy as np


class CompBlack:
    def __init__(self, strategy):
        self.strategy = strategy

    def decision(self, value, rem_races, races_number):
        if self.choice == -1:
            if self.strategy == "optimal":
                if self.player_choice == -1:
                    if value >= (1 - white_win_prob(rem_races - 1)) ** (1 / (rem_races - 1)) and rem_races != 2:
                        self.choice = value
                        print("Computer chose this value.")
                    elif rem_races == 2:
                        self.choice = value
                        print("Computer chose this value.")
                if self.player_choice != -1:
                    if value > self.player_choice:
                        self.choice = value
                        print("Computer chose this value.")
            elif self.strategy == "secretary":
                if rem_races > np.exp ** (-1) * races_number:
                    pass

    choice = -1
    player_choice = -1


class CompWhite:
    def __init__(self, strategy):
        self.strategy = strategy

    def decision(self, value, rem_races, races_number):
        if self.choice == -1:
            if self.strategy == "optimal":
                if self.player_choice == -1 and rem_races > 1 and value >= 0.5 ** (1 / (rem_races - 1)):
                    self.choice = value
                    print("Computer chose this value.")
                    self.choice_flag = 1
                elif self.player_choice != -1 and rem_races > 1:
                    if value > self.player_choice:
                        self.choice = value
                        print("Computer chose this value.")
                elif rem_races == 1:
                    self.choice = value
                    print("Computer chose this value.")
                else:
                    print("Computer didn't choose this value.")
            elif self.strategy == "secretary":
                if rem_races > np.exp ** (-1) * races_number:
                    pass
        elif self.choice != -1:
            self.choice_flag = 0
            print("Computer didn't choose this value.")

    choice = -1
    player_choice = -1
    choice_flag = 0


def white_win_prob(N):  # We can compute values for n - 1 numbers at the start and keep it in an array to optimize code
    if N == 1:
        return 1
    else:
        return (1 / N) + ((N - 1) / N) * ((0.5 ** (1 / (N - 1))) - ((1 - white_win_prob(N - 1)) ** (N / (N - 1))))


def single_round_black_bot(maximum_round, race_number, computer):
    i = maximum_round - race_number
    speed = rand.random()
    print(f"The average speed in the round {race_number + 1} was {speed}")
    if computer.player_choice == -1:
        print("Do you want to claim this round?")
        player_flag = str(input("Y/N: "))
        if player_flag == 'Y':
            computer.player_choice = speed
            player_flag = 1
        if player_flag != 'Y':
            computer.decision(speed, i, maximum_round)
    elif computer.player_choice != -1 and computer.choice == -1:
        computer.decision(speed, i, maximum_round)


def single_round_white_bot(maximum_round, race_number, computer):
    i = maximum_round - race_number
    speed = rand.random()
    print(f"The average speed in the round {race_number + 1} was {speed}")
    computer.decision(speed, i, maximum_round)
    if computer.choice_flag == 0 and computer.player_choice == -1:
        print("Do you want to claim this round?")
        player_flag = str(input("Y/N: "))
        if player_flag == 'Y':
            computer.player_choice = speed


print(
    "Hello, welcome to the:\nH O R S E    G  A M E\nYour objective is to bet a higher randomly generated number from "
    "0 to 1 "
    "than your opponent, which is the computer.\n")

number_of_races = int(input("Choose the amount of generated numbers: "))
player_side = input("Do you want to play as white (you'll have a priority in choice) or black? (W/B): ")

if player_side == "W":
    bot = CompBlack("optimal")
    for r in range(number_of_races):
        single_round_black_bot(number_of_races, r, bot)
elif player_side == "B":
    bot = CompWhite("optimal")
    for r in range(number_of_races):
        single_round_white_bot(number_of_races, r, bot)
else:
    print("Wrong side selection. Bye!")
    exit()

winner = "null"
if bot.player_choice > bot.choice:
    winner = "Y O U   W O N !!!"
else:
    winner = "Computer won :["
print(f"\nYour score: {bot.player_choice}\nComputer score: {bot.choice}")
print(f"\n{winner}")

# Calculation of probabilities, whete N is a number of races
# white_probs = [1]
# for i in range(2,N+1):
#     pre = white_probs[-1]
#     prob = (1 / i) + ((i - 1) / i) * ((0.5 ** (1 / (i - 1))) - ((1 - pre) ** (i / (i - 1))))
#     white_probs.append(prob.__round__(4))

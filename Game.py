import random as rand
import numpy as np
import csv
import time
import re


def YNCheck(val):
    if re.match("^[Y|N|n|y]$", val):
        return val.upper()
    else:
        val = input("Answer should be Y or N:  ")
        return YNCheck(val)


def CheckNumber(val):
    if re.match("^[1-5]{1,1}$", val):
        return int(val)
    else:
        val = input("Your choose should be in range 1 to 5: ")
        return CheckNumber(val)


def WBCheck(val):
    if re.match("^[W|B]$", val):
        return val.upper()
    else:
        val = input("Answer should be W or B: ")
        return WBCheck(val)


def GndrCheck(val):
    if re.match("^[M|F|O|m|f|o]$", val):
        return val.upper()
    else:
        val = input("Answer should be M, F or O: ")
        return GndrCheck(val)


class CompBlack:
    def __init__(self, strategy):
        self.strategy = strategy

    def decision(self, value, rem_races, races_number):
        if self.choice == -1:
            if self.strategy == "optimal":
                if self.player_choice == -1:
                    if value >= (1 - white_win_prob(rem_races - 1)) ** (1 / (rem_races - 1)) and rem_races != 2:
                        self.choice = value
                        print("\nComputer chose this value.\n")
                    elif rem_races == 2:
                        self.choice = value
                        print("\nComputer chose this value.\n")
                if self.player_choice != -1:
                    if value > self.player_choice or rem_races == 1:
                        self.choice = value
                        print("\nComputer chose this value.\n")
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
                    print("\nComputer chose this value.\n")
                    self.choice_flag = 1
                elif self.player_choice != -1 and rem_races > 1:
                    if value > self.player_choice:
                        self.choice = value
                        print("\nComputer chose this value.\n")
                elif rem_races == 1:
                    self.choice = value
                    print("\nComputer chose this value.\n")
                else:
                    print("\nComputer didn't choose this value.\n")
            elif self.strategy == "secretary":
                if rem_races > np.exp ** (-1) * races_number:
                    pass
        elif self.choice != -1:
            self.choice_flag = 0
            print("\nComputer didn't choose this value.\n")

    choice = -1
    player_choice = -1
    choice_flag = 0


def white_win_prob(N):  # We can compute values for n - 1 numbers at the start and keep it in an array to optimize code
    if N == 1:
        return 1
    else:
        return (1 / N) + ((N - 1) / N) * ((0.5 ** (1 / (N - 1))) - ((1 - white_win_prob(N - 1)) ** (N / (N - 1))))


def single_round_black_bot(maximum_round, race_number, computer, register):
    i = maximum_round - race_number
    speed = round(register[race_number], 4)
    print(f"The average speed in the round {race_number + 1} was {speed}")
    if computer.player_choice == -1:
        print("Do you want to claim this round?")
        player_flag = YNCheck(input("Y/N: "))
        if player_flag == 'Y':
            computer.player_choice = speed
            return (race_number + 1)
        if player_flag != 'Y':
            computer.decision(speed, i, maximum_round)
    elif computer.player_choice != -1 and computer.choice == -1:
        computer.decision(speed, i, maximum_round)


def single_round_white_bot(maximum_round, race_number, computer, register):
    i = maximum_round - race_number
    speed = round(register[race_number], 4)
    print(f"The average speed in the round {race_number + 1} was {speed}")
    computer.decision(speed, i, maximum_round)
    if computer.choice_flag == 0 and computer.player_choice == -1:
        print("Do you want to claim this round?")
        player_flag = YNCheck(input("Y/N: ")).upper()
        if player_flag == 'Y':
            computer.player_choice = speed
            return (race_number + 1)


speeds = np.loadtxt('speeds.csv')

print(
    "\n\nHello, welcome to the:\nH O R S E    G  A M E\nYour objective is to bet a higher randomly generated number from 0 to 1 "
    "than your opponent, which is the computer.\n")

initials = input("How should we call you: ")
gender = GndrCheck(input("Please select your gender. M = Male / F = Female / O = Other: "))
game_mode = YNCheck(input("Would you like to play a testing mode? (Y/N):"))
if game_mode == 'Y':
    number_of_races = int(input("Choose the amount of generated numbers: "))
    speed_table = [rand.random() for i in range(number_of_races)]
else:
    number_of_races = 10
    print(
        f"You'll play exactly {number_of_races} rounds. If you don't choose any value until the end of the game, you lose!")
    k = CheckNumber(input("Choose a game set you want to play (1-5): "))
    speed_table = speeds[k - 1]
player_side = WBCheck(input("Do you want to play as white (you'll have a priority in choice) or black? (W/B): "))

choice = 0
if player_side == "W":
    bot = CompBlack("optimal")
    for r in range(number_of_races):
        time.sleep(1)
        temp = single_round_black_bot(number_of_races, r, bot, speed_table)
        if temp is not None: choice = temp

elif player_side == "B":
    bot = CompWhite("optimal")
    for r in range(number_of_races):
        time.sleep(1)
        temp = single_round_white_bot(number_of_races, r, bot, speed_table)
        if temp is not None: choice = temp

else:
    print("Wrong side selection. Bye!")
    exit()

winner = "null"
f = open('game_data.csv', 'a')
writer = csv.writer(f, delimiter=',')
speed_set = 0
if bot.player_choice > bot.choice:
    winner = "Y O U   W O N !!!"

    if game_mode == "N": writer.writerow((initials, player_side, choice, k, 1, gender))

else:
    winner = "Computer won :["

    if game_mode == "N": writer.writerow((initials, player_side, choice, k, 0, gender))
print(f"\nYour score: {bot.player_choice}\nComputer score: {bot.choice}")
print(f"\n{winner}")

f.close()

# generated speeds for games and probs for white
white_win_probs = np.array(
    [1.0, 0.75, 0.7214045, 0.7088087, 0.7015923, 0.6968756, 0.6935346, 0.6910357, 0.6890915, 0.687533])



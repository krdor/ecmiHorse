import random as rand


class Player:
    def __init__(self, name):
        self.name = name

    choice = -1
    choice_moment = 0


def single_round(player_w, player_b, max, curr, reg, rej_prob_flg):
    speed = reg[curr]
    print(f"The average speed in the round {curr + 1} was {speed}")
    if player_w.choice == -1 and player_b.choice == -1 and rej_prob_flg == 1:
        reject_prob = rand.random()
        print(f"{player_w.name}, there is {round(reject_prob * 100)}% risk your choice will be rejected!")
        flg = input(f"{player_w.name}, do you want to claim this number? Y/N: ")
        if flg == 'Y':
            if rand.random() > reject_prob:
                player_w.choice = speed
                player_w.choice_moment = curr
            else:
                print(f"Sorry {player_w.name} your choice have been rejected :(")
                flg = input(f"{player_b.name}, do you want to claim this number? Y/N: ")
            if flg == 'Y':
                player_b.choice = speed
                player_b.choice_moment = curr
        elif flg == 'N':
            flg = input(f"{player_b.name}, do you want to claim this number? Y/N: ")
            if flg == 'Y':
                player_b.choice = speed
                player_b.choice_moment = curr
    elif player_w.choice == -1 and player_b.choice == -1 and rej_prob_flg == 0:
        flg = input(f"{player_w.name}, do you want to claim this number? Y/N: ")
        if flg == 'Y':
            player_w.choice = speed
            player_w.choice_moment = curr
        elif flg == 'N':
            flg = input(f"{player_b.name}, do you want to claim this number? Y/N: ")
            if flg == 'Y':
                player_b.choice = speed
                player_b.choice_moment = curr
    elif player_w.choice == -1 and player_b.choice != -1:
        flg = input(
            f"{player_b.name}'s choice is {player_b.choice}.\n{player_w.name}, do you want to claim this number? Y/N: ")
        if flg == 'Y':
            player_w.choice = speed
            player_w.choice_moment = curr
    elif player_w.choice != -1 and player_b.choice == -1:
        flg = input(
            f"{player_w.name}'s choice is {player_w.choice}.\n{player_b.name}, do you want to claim this number? Y/N: ")
        if flg == 'Y':
            player_b.choice = speed
            player_b.choice_moment = curr
    else:
        pass


print(
    "Hello, welcome to the:\n\nH O R S E    G  A M E\n\nYour objective is to bet a higher randomly generated number from 0 to 1 "
    "than your opponent!\n")

player_one_name = input("Please input a name for player 1: ")
player_two_name = input("Please input a name for player 2: ")

option_side_selection_method = input(
    "If you want to do side selection yourself type 'Y', if you want it to be random type 'R': ")

if option_side_selection_method == 'R':
    if rand.randint(0, 1) == 0:
        white = Player(player_one_name)
        print(f"{player_one_name} is playing as white")
        black = Player(player_two_name)
        print(f"{player_two_name} is playing as black")
    else:
        white = Player(player_two_name)
        print(f"{player_two_name} is playing as white")
        black = Player(player_one_name)
        print(f"{player_one_name} is playing as black")
elif option_side_selection_method == 'Y':
    side_select_flag = input(f"Should {player_one_name} be on white side? Y/N: ")
    if side_select_flag == 'Y':
        white = Player(player_one_name)
        print(f"{player_one_name} is playing as white")
        black = Player(player_two_name)
        print(f"{player_two_name} is playing as black")
    elif side_select_flag == 'N':
        white = Player(player_two_name)
        print(f"{player_two_name} is playing as white")
        black = Player(player_one_name)
        print(f"{player_one_name} is playing as black")

number_of_rounds = int(input("How many rounds would you like to play? (We recommend around 10): "))

speed_table = [round(rand.random(), 4) for i in range(number_of_rounds)]

option_reject = 0
if input("Do you want to enable probability of white choice to be rejected? Y/N: ") == 'Y':
    option_reject = 1

option_switch = 0
if input("Do you want to enable priority switching between rounds?? Y/N: ") == 'Y':
    option_switch = 1

for rnd in range(number_of_rounds):
    if option_switch == 0:
        single_round(white, black, number_of_rounds, rnd, speed_table, option_reject)
    elif option_switch == 1:
        if rnd % 2 == 0:
            single_round(white, black, number_of_rounds, rnd, speed_table, option_reject)
        elif rnd % 2 == 1:
            single_round(black, white, number_of_rounds, rnd, speed_table, option_reject)

if white.choice > black.choice:
    print(f"\n{white.name} won!!!")
elif white.choice < black.choice:
    print(f"\n{black.name} won!!!")
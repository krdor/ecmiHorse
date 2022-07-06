import os
import re


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def CheckNumber(val):
    if re.match("^[1-2]{1,1}$", val):
        return int(val)
    else:
        val = input("Your choose should be in range 1 to 2: ")
        return CheckNumber(val)


def start():
    print('\nHey!')
    print("\nChoose the game you want to play: \n\n1 - Playing against computer\n2 - Playing against partner")
    number = CheckNumber(input("\nСhoose the appropriate option: "))
    if number == 1:
        os.system('python Game.py')

        again()
    elif number == 2:

        os.system('python P2PGame.py')
        again()
    else:
        print("Incorrect symbol!")


def again():
    print("\n\nDo you want to play again:\n1 - yes\n2 - no")
    choice = CheckNumber(input(""))
    if choice == 1:
        cls()
        start()

    elif choice == 2:
        exit()


start()
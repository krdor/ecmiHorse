import random as rand


def white_win_prob(N):  # We can compute values for n - 1 numbers at the start and keep it in an array to optimize code
    if N == 1:
        return 1
    else:
        return (1/N) + ((N-1)/N) * ((0.5 ** (1 / (N-1))) - ((1 - white_win_prob(N-1)) ** (N / (N-1))))


def single_simulation(n):
    white_choice = -1
    black_choice = -1

    for temp in range(n - 1):
        speed = rand.random()
        i = n - temp
        flag = 0
        if white_choice == -1:
            if speed >= 0.5 ** (1 / (i - 1)):
                white_choice = speed
                flag = 1
        if flag == 0 and black_choice == -1 and i != 2:
            if speed >= (1 - white_win_prob(i - 1)) ** (1 / (i - 1)):
                black_choice = speed
        elif flag == 0 and black_choice == -1 and i == 2:
            black_choice = speed

    final_race = rand.random()
    if white_choice == -1:
        white_choice = final_race
    if black_choice == -1:
        black_choice = final_race

    if white_choice > black_choice:
        return 1
    else:
        return 0


number_of_races = 100
result = 0
num_of_mc_steps = 100000
for step in range(num_of_mc_steps):
    result += single_simulation(number_of_races)

print(f"Probability of white win: {result/num_of_mc_steps}")






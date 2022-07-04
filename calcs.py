def white_win_prob(N):  # We can compute values for n - 1 numbers at the start and keep it in an array to optimize code
    if N == 1:
        return 1
    else:
        return (1/N) + ((N-1)/N) * ((0.5 ** (1 / (N-1))) - ((1 - white_win_prob(N-1)) ** (N / (N-1))))

print(white_win_prob(10))
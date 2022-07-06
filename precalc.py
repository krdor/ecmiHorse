# import numpy as np
# import pandas as pd

# just a function to generate speeds
# pd.DataFrame(np.random.rand(5,10)).to_csv("./speeds.csv", header = False,sep='\t', index=False)


# white_probs = [1]
# for i in range(2,11):
#     pre = white_probs[-1]
#     prob = (1 / i) + ((i - 1) / i) * ((0.5 ** (1 / (i - 1))) - ((1 - pre) ** (i / (i - 1))))
#     white_probs.append(prob.__round__(7))

# pd.DataFrame(list(white_probs)).to_csv("./probs.csv", header = False,sep=',', index=False)

# import python-csv as csv
# import re


# val = YNCheck(input("Choose"))
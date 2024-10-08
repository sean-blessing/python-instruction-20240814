import pandas as pd
# from printheader import print_header


cols = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']  # column names
indices = ['a', 'b', 'c', 'd', 'e', 'f']  # row names

values = [  # sample data
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]
print('cols')
print(cols, '\n')

print('indices')
print(indices, '\n')

print('values')
print(values, '\n')

df = pd.DataFrame(values, index=indices, columns=cols)  # create dataframe with row and column names
print('DataFrame df')
print(df, '\n')

print("df['gamma']")
print(df['gamma'])  # select column 'gamma'

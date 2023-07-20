import pandas as pd

df = pd.read_csv('output.csv')

avg = df.iloc[:, 1].mean()

print(avg)

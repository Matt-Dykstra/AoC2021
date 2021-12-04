import pandas as pd
df = pd.read_csv('day2_input.txt', sep=" ",header=None)
df=df.rename(columns={0: "dir", 1:"dist"})

df2 = df.groupby("dir").sum()
answer = (df2.loc['down']-df2.loc['up'])*df2.loc['forward']
print(answer['dist'])





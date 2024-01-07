import pandas as pd

df = pd.read_csv("nba.csv", sep = ",")
print (df[df["Age"] == 30] )
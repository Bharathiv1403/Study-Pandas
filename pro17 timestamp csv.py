import pandas as pd 
df = pd.read_csv("Movies.csv") 

df['timestamp'] = df['timestamp'] - df['timestamp'].shift(1)
print(df.to_string())
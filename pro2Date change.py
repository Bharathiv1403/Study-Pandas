import pandas as pd
df=pd.read_csv("dirtydata.csv")
df[ 'Date'] = pd. to_datetime(df['Date'])
df.dropna(subset=["Date"])
print(df.to_string)
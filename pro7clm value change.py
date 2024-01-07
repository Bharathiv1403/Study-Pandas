import pandas as pd
df=pd.read_csv("dirtydata.csv")
df.loc[7,"Duration"]=120
print(df.to_string())
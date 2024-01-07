#Value change the column
import pandas as pd
df=pd.read_csv("dirtydata.csv")
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=110
print(df)
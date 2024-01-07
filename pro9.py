#Row Removing the Csv file
import pandas as pd
df=pd.read_csv("dirtydata.csv")
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)
print(df)
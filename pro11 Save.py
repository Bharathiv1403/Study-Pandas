#Save the Csv file
import pandas as pd
df=pd.read_csv("dirtydata.csv")
df.fillna(1001,inplace=True)
print(df)
df.to_csv("Filedata.csv")
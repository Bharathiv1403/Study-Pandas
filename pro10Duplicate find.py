#Duplicate find
import pandas as pd
df=pd.read_csv("dirtydata.csv")
x=df.duplicated()
print(x)
# Duplicate row remove 
import pandas as pd
df=pd.read_csv("dirtydata.csv")
df.drop_duplicates(inplace=True)
print(df)
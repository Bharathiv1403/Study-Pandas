#Alphabet order
import pandas as pd 
# making data frame 
data = pd.read_csv("nba.csv")
a = data.Name.values.astype(str).argsort()
data=pd.DataFrame(data.values[a], data.index[a], data.columns)
print(data.to_string())


# #Number order
# import pandas as pd 
# df = pd.read_csv("nba.csv")
# a = df.Number.values.astype(int).argsort()
# df=pd.DataFrame(df.values[a], df.index[a], df.columns)
# print(df.to_string())
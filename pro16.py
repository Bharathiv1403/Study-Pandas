import pandas as pd
# reading csv file from url 
data=pd.read_csv("nba.csv")
# dropping null value columns to avoid errors
data.dropna(inplace = True)
# substring to be searched
sub ='A'
# creating and passing series to new column
data["Indexes"]= data["Name"].str.find(sub)
print(data.to_string())
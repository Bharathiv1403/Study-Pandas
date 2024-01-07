from datetime import datetime
import pandas as pd
df=pd.read_csv("movielens.csv")
#Getting Datetime from timestamp
date_time = datetime.fromtimestamp(df,"timestamp") #1704365264
print("Datetime from timestamp:", date_time)
print("Current Time : ",date_time.time)
import calendar, time; calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))
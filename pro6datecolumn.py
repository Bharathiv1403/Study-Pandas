import pandas as pd
# import numpy as np
dates = pd.date_range("20130101", periods=6)
x=pd.DataFrame(dates)
print("Date: ",x.to_string())
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(dates)
# x=np.random.rand(d0, d1, ..., dn)
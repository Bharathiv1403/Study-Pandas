import matplotlib.pyplot as plt
year = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
unemployment_rate = [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
plt.plot(year, unemployment_rate)
plt.title('unemployment rate vs year')
plt.xlabel('year')
plt.ylabel('unemployment rate')
plt.show()
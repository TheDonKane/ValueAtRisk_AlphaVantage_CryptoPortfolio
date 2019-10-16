#Data manipulation
import numpy as np
import pandas as pd

#Plotting
import matplotlib.pyplot as plt
import seaborn

#Data fetching
import yfinance as yf
#from alpha_vantage.timeseries import TimeSeries

#Print tabular data
from tabulate import tabulate

#Calculate daily returns
df = yf.download('GOOG')
df = yf.download('MSFT')
df = yf.download('AAPL')
df['returns'] = df.Close.pct_change()
df = df.dropna()
plt.hist(df.returns, bins=40)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#Sort the returns
df.sort_values('returns', inplace = True, ascending = True)

#Calculate Value at Risk
VaR_90 = df['returns'].quantile(0.1)
VaR_95 = df['returns'].quantile(0.05)
VaR_99 = df['returns'].quantile(0.01)

print (tabulate([['Confidence Level', 'Value at Risk'], ['90%', VaR_90], ['95%', VaR_95], ['99%', VaR_99]], headers ="firstrow"))

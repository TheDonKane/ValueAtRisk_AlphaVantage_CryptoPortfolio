#Data manipulation
import numpy as np
import pandas as pd

#Plotting
from matplotlib import mlab
import matplotlib.pyplot as plt
import seaborn
from scipy.stats import norm

#Data fetching
from alpha_vantage.cryptocurrencies import CryptoCurrencies

#Print tabular data
from tabulate import tabulate

#API key
api_key = 'USYAK8KB5VER3M1P'

#pull Data
cc = CryptoCurrencies(key=api_key, output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')

#Calculate daily returns
df = data['4a. close (USD)']

percentage = df.pct_change()

print(percentage[1:])

#Sort the returns
#df.sort_values(percentage, inplace = True, ascending = True)

#Calculate Value at Risk
VaR_90 = percentage.quantile(0.1)
VaR_95 = percentage.quantile(0.05)
VaR_99 = percentage.quantile(0.01)

print (tabulate([['Confidence Level', 'Value at Risk'], ['90%', VaR_90], ['95%', VaR_95], ['99%', VaR_99]], headers ="firstrow"))


#plot histogram
mean = np.mean(percentage)
std_dev = np.std(percentage)
percentage.hist(bins=50)
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
plt.plot(x,mlab.normpdf(x, mean, std_dev), "r" )
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()

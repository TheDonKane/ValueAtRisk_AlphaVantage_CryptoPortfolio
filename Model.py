#Data manipulation
import numpy as np
import pandas as pd

#Plotting
import matplotlib.pyplot as plt
import seaborn

#Data fetching
from alpha_vantage.cryptocurrencies import CryptoCurrencies

#API key
api_key = 'USYAK8KB5VER3M1P'

#pull Data
cc = CryptoCurrencies(key=api_key, output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')
data['4b. close (USD)']
print(data)

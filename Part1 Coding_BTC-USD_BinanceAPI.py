#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import pandas as pd
from datetime import datetime

# Binance API endpoint for historical kline/candlestick data
url = 'https://api.binance.com/api/v3/klines'

# Parameters for API request
params = {
    'symbol': 'BTCUSDT',  # Corrected symbol format
    'interval': '1m',      # 1-minute candles granularity
    'limit': 1000          # Number of data points to fetch (max 1000)
}

# Make API request
response = requests.get(url, params=params)
data = response.json()

# Check if API response contains data
if isinstance(data, list) and len(data) > 0:
    # Convert data to DataFrame for easier processing
    df = pd.DataFrame(data, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'])

    # Convert timestamps to datetime objects
    df['Candle Open Time'] = df['Open Time'].apply(lambda x: datetime.utcfromtimestamp(int(x) // 1000).strftime('%Y-%m-%d %H:%M:%S'))
    df['Candle Close Time'] = df['Close Time'].apply(lambda x: datetime.utcfromtimestamp(int(x) // 1000).strftime('%Y-%m-%d %H:%M:%S'))

    # Select required columns and reorder them
    df = df[['Open', 'Close', 'High', 'Low', 'Volume', 'Quote Asset Volume', 'Number of Trades', 'Candle Open Time', 'Candle Close Time']]
    
    # Add Trading Pair column with constant value
    df['Trading Pair'] = 'BTCUSD'

    # Rename columns
    df.columns = ['Open Price', 'Close Price', 'High Price', 'Low Price', 'BTC Volume', 'USD Volume', 'Number of Trades', 'Candle Open Time', 'Candle Close Time', 'Trading Pair']

    # Store data in Data Lake (Assuming CSV format for simplicity)
    df.to_csv('btc_usd_data.csv', index=False)
    
    print("Data successfully retrieved and stored.")
else:
    print("Error: Invalid symbol or empty response from Binance API.")


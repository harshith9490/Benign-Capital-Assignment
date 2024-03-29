import requests
import pandas as pd
import numpy as np

# Define the API endpoint
# Defining the Query Parameters
endpoint = 'https://www.alphavantage.co/query'
query_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': 'IBM',
    'interval': '5min',
    'apikey': 'demo'
}

# Send a GET request to the API endpoint with the query parameters
response = requests.get(endpoint, params=query_params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response and convert to a pandas DataFrame
    data = response.json()['Time Series (5min)']
    df = pd.DataFrame.from_dict(data, orient='index').astype(float)
    df.index = pd.to_datetime(df.index)

    # Calculate the SuperTrend indicator
    atr_period = 7
    multiplier = 3
    df['TR'] = np.maximum.reduce([
        df['2. high'] - df['3. low'],
        np.abs(df['2. high'] - df['4. close'].shift()),
        np.abs(df['3. low'] - df['4. close'].shift())
    ])
    df['ATR'] = df['TR'].rolling(atr_period).mean()
    df['UpperBand'] = (df['2. high'] + df['3. low']) / 2 + multiplier * df['ATR']
    df['LowerBand'] = (df['2. high'] + df['3. low']) / 2 - multiplier * df['ATR']
    df['initial super trend']=0
    df['SuperTrend'] = np.where(df['4. close'] > df['initial super trend'].shift(), df['LowerBand'], df['UpperBand'])

    
print(df['SuperTrend'])

import pandas as pd
import requests
import defs

session = requests.Session()  # create session so we can request alot without being blocked
instrument = "EUR_USD"
count = 1000
granularity = "S5"

url = f'{defs.OANDA_URL}/instruments/{instrument}/candles'

params = dict(

    count=count,
    granularity=granularity,
    price="MBA"

)

response = session.get(url, params=params, headers=defs.SECURE_HEADER)

data = response.json()
prices = ['mid', 'bid', 'ask']
ohlc = ['o', 'h', 'l', 'c']

our_data = list()
for candle in data['candles']:
    if not candle['complete']:
        continue
    new_dict = dict()
    new_dict['time'] = candle['time']
    new_dict['volume'] = candle['volume']
    for price in prices:
        for oh in ohlc:
            new_dict[f'{price}_{oh}'] = candle[price][oh]

    our_data.append(new_dict)


candles_df = pd.DataFrame.from_dict(our_data)
candles_df.to_csv("EUR_USD.csv", index=False)

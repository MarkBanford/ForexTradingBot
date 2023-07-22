import requests
import defs
import pandas as pd

session = requests.Session()  # create session so we can request alot without being blocked

url = f'{defs.OANDA_URL}/accounts/{defs.ACCOUNT_ID}/instruments'

response = session.get(url, params=None, headers=defs.SECURE_HEADER)

data = response.json()

instruments = data['instruments']

instrument_data = []

for item in instruments:
    new_obj = dict(
        name=item['name'],
        type=item['type'],
        displayName=item['displayName'],
        pipLocation=item['pipLocation'],
        marginRate=item['marginRate']
    )
    instrument_data.append(new_obj)

instrument_df = pd.DataFrame.from_dict(instrument_data)

instrument_df.to_pickle('instrument.pkl')
instrument_df.to_csv('instrument.csv', index=False)

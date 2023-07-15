import requests
import defs

session = requests.Session()  # create session so we can request alot without being blocked

url = f'{defs.OANDA_URL}/accounts/{defs.ACCOUNT_ID}/instruments'

response = session.get(url, params=None, headers=defs.SECURE_HEADER)

data = response.json()

instruments = data['instruments']
print(instruments[0].keys())

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

for i in instrument_data:
    print(i)

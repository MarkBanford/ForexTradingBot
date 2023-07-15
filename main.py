import requests
import defs

session = requests.Session()  # create session so we can request alot without being blocked
instrument = "EUR_USD"
count = 10
granularity = "H1"

url = f'{defs.OANDA_URL}/instruments/{instrument}/candles'

params = dict(

    count=count,
    granularity=granularity,
    price="MBA"

)

response = session.get(url, params=params, headers=defs.SECURE_HEADER)

print(response.status_code)

print(response.json())

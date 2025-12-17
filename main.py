from binance import Client


client = Client(api_key='', api_secret='')

prices = client.get_all_tickers()
from binance.client import Client

client = Client()  # для публічних даних API ключі не потрібні

# client = Client(api_key='', api_secret='')

# prices = client.get_all_tickers()

def get_price(symbol: str):
    data = client.get_symbol_ticker(symbol=symbol)
    return float(data['price'])

print(get_price("BTCUSDT"))

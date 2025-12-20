import requests
from binance.client import Client

binance_client = Client()  # для публічних даних API ключі не потрібні

url = "https://api.bybit.com/v5/market/tickers"
params = {"category": "spot"}


def get_price_binance(symbol: str):
    name = binance_client.get_symbol_ticker(symbol=symbol)
    addbid = binance_client.get_orderbook_tickers(symbol=symbol)
    return name['symbol'], float(addbid['askPrice']), float(addbid['bidPrice'])


r = requests.get(url, params=params).json()


def get_price_bybit(t):
    for t in r["result"]["list"]:
        if t["symbol"].endswith("USDT") and t["symbol"] == 'BTCUSDT':
            bybit_price = (
                t["symbol"],
                t["bid1Price"],
                t["ask1Price"]
            )
    return bybit_price


# prices = {
#     'Binance': get_price_binance,
#     'Bybit': get_price_bybit,
# }

# Fees for binance, bybit and others cryptocurrency exchange
# fees = {
#     'Binance': '0.01',
#     'Bybit': '0.01',
# }

# print(prices['Binance']('BTCUSDT'), prices['Bybit']('BTCUSDT'))


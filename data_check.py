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


def get_price_bybit(symbol: str):
    r = requests.get(url, params=params, timeout=5).json()

    for item in r["result"]["list"]:
        if item["symbol"] == symbol:
            return (
                item["symbol"],
                float(item["bid1Price"]),
                float(item["ask1Price"])
            )





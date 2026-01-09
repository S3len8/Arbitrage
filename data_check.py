import requests
from binance.client import Client

binance_client = Client()  # для публічних даних API ключі не потрібні


def get_price_binance(symbols: list[str]) -> dict:
    data = binance_client.get_orderbook_tickers()
    result = {}

    for item in data:
        symbol = item["symbol"]
        if symbol in symbols:
            result[symbol] = {
                "bid": float(item["bidPrice"]),
                "ask": float(item["askPrice"])
            }

    return result


def get_price_bybit(symbols: list[str]) -> dict:
    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": "spot"}

    r = requests.get(url, params=params, timeout=5).json()
    result = {}

    for item in r["result"]["list"]:
        symbol = item["symbol"]
        if symbol in symbols:
            result[symbol] = {
                "bid": float(item["bid1Price"]),
                "ask": float(item["ask1Price"])
            }

    return result


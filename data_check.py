import requests
from binance.client import Client

binance_client = Client()  # для публічних даних API ключі не потрібні


def get_price_binance():
    data = binance_client.get_orderbook_tickers()
    result = {}

    for item in data:
        symbol = item["symbol"]
        if symbol.endswith("USDT"):
            result[symbol] = {
                "bid": float(item["bidPrice"]),
                "ask": float(item["askPrice"])
            }

    return result


def get_price_bybit(symbol: str):
    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": "spot"}
    r = requests.get(url, params=params, timeout=5).json()

    for item in r["result"]["list"]:
        if item["symbol"] == symbol:
            return (
                item["symbol"],
                float(item["bid1Price"]),
                float(item["ask1Price"])
            )


print(get_price_binance())



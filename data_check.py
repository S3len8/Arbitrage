import requests
from binance.client import Client

binance_client = Client()  # для публічних даних API ключі не потрібні


def get_binance_spot_symbols():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    data = requests.get(url).json()

    symbols = []
    for s in data["symbols"]:
        if s["status"] == "TRADING" and s["isSpotTradingAllowed"]:
            symbols.append({
                "symbol": s["symbol"],
                "base": s["baseAsset"],
                "quote": s["quoteAsset"]
            })
    return symbols


def get_bybit_spot_symbols():
    url = "https://api.bybit.com/v5/market/instruments-info"
    params = {"category": "spot"}

    data = requests.get(url, params=params).json()
    symbols = []

    for s in data["result"]["list"]:
        if s["status"] == "Trading":
            symbols.append({
                "symbol": s["symbol"],
                "base": s["baseCoin"],
                "quote": s["quoteCoin"]
            })
    return symbols


binance_symbols = get_binance_spot_symbols()
usdt_pairs = [s for s in binance_symbols if s["quote"] == "USDT"]
print(len(usdt_pairs))
print(usdt_pairs[:5])
bybit_symbols = get_bybit_spot_symbols()
bybit_usdt = [s for s in bybit_symbols if s["quote"] == "USDT"]
print(len(bybit_usdt))
print(bybit_usdt[:5])


def comparison_symbols(binance: list, bybit: list) -> list:
    binance_symbols = {x["symbol"] for x in binance}
    bybit_symbols = {x["symbol"] for x in bybit}

    common_symbols = binance_symbols & bybit_symbols

    return [x for x in binance if x["symbol"] in common_symbols]


common = comparison_symbols(usdt_pairs, bybit_usdt)
print(len(common))
print(common)


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


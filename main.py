import time

from data_check import get_price_binance, get_price_bybit

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

# prices = {
#     'Binance': get_price_binance,
#     'Bybit': get_price_bybit,
# }
#
# data_binance = list(prices['Binance']('BTCUSDT'))
# data_bybit = list(prices['Bybit']('BTCUSDT'))
#
# price_binance_bid, price_binance_ask = float(data_binance[2]), float(data_binance[1])
# price_bybit_bid, price_bybit_ask = float(data_bybit[1]), float(data_bybit[2])


# def calc_bid(firstCurrency, secondCurrency):
#     if firstCurrency > secondCurrency:
#         result = firstCurrency - secondCurrency
#         return result
#     if secondCurrency > firstCurrency:
#         result = secondCurrency - firstCurrency
#         return result
#
#
# def calc_ask(firstCurrency, secondCurrency):
#     if firstCurrency > secondCurrency:
#         result = firstCurrency - secondCurrency
#         return result
#     if secondCurrency > firstCurrency:
#         result = secondCurrency - firstCurrency
#         return result


def calc_spread(symbol, binance, bybit):
    if binance["bid"] > bybit["bid"]:
        spread = (binance["ask"] - bybit["bid"]) / binance["ask"]
        side = "BUY Bybit → SELL Binance"
    else:
        spread = (bybit["ask"] - binance["bid"]) / bybit["ask"]
        side = "BUY Binance → SELL Bybit"

    return side, spread * 100


while True:
    binance_data = get_price_binance(SYMBOLS)
    bybit_data = get_price_bybit(SYMBOLS)

    for symbol in SYMBOLS:
        if symbol not in binance_data or symbol not in bybit_data:
            continue

        side, spread = calc_spread(
            symbol,
            binance_data[symbol],
            bybit_data[symbol]
        )

        print(
            f"{symbol} | {side} | Spread: {spread:.4f}% | "
            f"Binance {binance_data[symbol]['bid']}/{binance_data[symbol]['ask']} | "
            f"Bybit {bybit_data[symbol]['bid']}/{bybit_data[symbol]['ask']}"
            f"\n ==============================================================="
        )

    time.sleep(7)









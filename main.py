import time

from data_check import get_price_binance, get_price_bybit

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]


def calc_spread(symbol, binance, bybit):
    if binance["bid"] > bybit["bid"]:
        spread = (binance["ask"] - bybit["bid"]) / binance["ask"]
        side = "BUY Bybit → SELL Binance"
    else:
        spread = (bybit["ask"] - binance["bid"]) / bybit["ask"]
        side = "BUY Binance → SELL Bybit"

    return side, spread * 100


def filter_spread():
    if spread > 0.02:
        print(f"Best spread is {symbol}")


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

        filter_spread()

        print(
            f"{symbol} | {side} | Spread: {spread:.4f}% | "
            f"Binance {binance_data[symbol]['bid']}/{binance_data[symbol]['ask']} | "
            f"Bybit {bybit_data[symbol]['bid']}/{bybit_data[symbol]['ask']}"
            f"\n ==============================================================="
        )

    time.sleep(7)









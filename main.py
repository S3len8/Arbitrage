import time

from data_check import get_price_binance, get_price_bybit, get_symbols


SYMBOLS = get_symbols()


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

        if spread > 0.64:
            print(
                f"{symbol} | {side} | Spread: {spread:.4f}% | "
                f"Binance buy: {binance_data[symbol]['bid']} / sell: {binance_data[symbol]['ask']} | "
                f"Bybit buy: {bybit_data[symbol]['bid']} / sell: {bybit_data[symbol]['ask']}"
                f"\n ==============================================================="
            )

    time.sleep(7)









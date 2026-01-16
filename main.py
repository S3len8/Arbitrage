import time

from data_check import get_price_binance, get_price_bybit, get_symbols


SYMBOLS = get_symbols()
fees = {
    'Binance': 0.1, 'Bybit': 0.1, 'Bitget': 0.1, 'Kucoin': 0.1, 'Mexc': 0.0, 'Gate': 0.1,
}


def calc_spread(symbol, binance, bybit, fees):
    if binance["bid"] > bybit["ask"]:
        spread = ((binance["bid"] - bybit["ask"]) / binance["bid"]) - fees['Binance'] - fees['Bybit']
        side = "BUY Bybit → SELL Binance"
    elif bybit["bid"] > binance["ask"]:
        spread = (bybit["bid"] - binance["ask"]) / bybit["bid"] - fees['Binance'] - fees['Bybit']
        side = "BUY Binance → SELL Bybit"
    else:
        return None, 0.0

    return side, spread * 100


try:
    while True:
        binance_data = get_price_binance(SYMBOLS)
        bybit_data = get_price_bybit(SYMBOLS)

        for symbol in SYMBOLS:
            if symbol not in binance_data or symbol not in bybit_data:
                continue

            side, spread = calc_spread(
                symbol,
                binance_data[symbol],
                bybit_data[symbol],
                fees,
            )

            if spread > 0.17:
                print(
                    f"{symbol} | {side} | Spread: {spread:.4f}% | "
                    f"Binance {binance_data[symbol]['bid']} / {binance_data[symbol]['ask']} | "
                    f"Bybit {bybit_data[symbol]['bid']} / {bybit_data[symbol]['ask']}" 
                    f""
                    f"\n ==============================================================="
                )

        time.sleep(7)
except KeyboardInterrupt as e:
    print("Program ended!")









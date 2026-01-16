import time

from data_check import get_price_binance, get_price_bybit, get_symbols, get_price_bitget


SYMBOLS = get_symbols()
fees = {
    'Binance': 0.1, 'Bybit': 0.1, 'Bitget': 0.1, 'Kucoin': 0.1, 'Mexc': 0.0, 'Gate': 0.1,
}


def check_pair(ex1_name, ex1, ex2_name, ex2, fees):
    if not ex1 or not ex2:
        return None, 0.0

    # BUY ex2 → SELL ex1
    if ex1["bid"] > ex2["ask"]:
        spread = (
            (ex1["bid"] - ex2["ask"]) / ex1["bid"]
            - fees[ex1_name] / 100
            - fees[ex2_name] / 100
        )
        return f"BUY {ex2_name} → SELL {ex1_name}", spread

    # BUY ex1 → SELL ex2
    if ex2["bid"] > ex1["ask"]:
        spread = (
            (ex2["bid"] - ex1["ask"]) / ex2["bid"]
            - fees[ex1_name] / 100
            - fees[ex2_name] / 100
        )
        return f"BUY {ex1_name} → SELL {ex2_name}", spread

    return None, 0.0


# ─────────────────────────────────────────────
# Поиск ЛУЧШЕГО спреда среди всех бирж
# ─────────────────────────────────────────────
def calc_spread(symbol, prices: dict, fees):
    best_side = None
    best_spread = 0.0

    names = list(prices.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            side, spread = check_pair(
                names[i],
                prices[names[i]],
                names[j],
                prices[names[j]],
                fees,
            )

            if spread > best_spread:
                best_spread = spread
                best_side = side

    return best_side, best_spread * 100


# ─────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────
try:
    while True:
        binance_data = get_price_binance(SYMBOLS)
        bybit_data = get_price_bybit(SYMBOLS)
        bitget_data = get_price_bitget(SYMBOLS)

        for symbol in SYMBOLS:
            if (
                symbol not in binance_data
                or symbol not in bybit_data
                or symbol not in bitget_data
            ):
                continue

            prices = {
                "Binance": binance_data[symbol],
                "Bybit": bybit_data[symbol],
                "Bitget": bitget_data[symbol],
            }

            side, spread = calc_spread(symbol, prices, fees)

            if spread > 0.17:
                print(
                    f"{symbol} | {side} | Spread: {spread:.4f}%\n"
                    f"Binance: {prices['Binance']['bid']} / {prices['Binance']['ask']}\n"
                    f"Bybit:   {prices['Bybit']['bid']} / {prices['Bybit']['ask']}\n"
                    f"Bitget:  {prices['Bitget']['bid']} / {prices['Bitget']['ask']}\n"
                    f"{'=' * 60}"
                )

        time.sleep(7)

except KeyboardInterrupt:
    print("Program ended!")








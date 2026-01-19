import time

from data_check import get_price_binance, get_price_bybit, get_symbols, get_price_bitget, NETWORK_CACHE

min_spread = float(input("Spread: "))

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


def extract_asset(symbol: str) -> str:
    """
    Selects the base coin from the trading pair.
    Example: BTCUSDT -> BTC, ETHBUSD -> ETH
    """
    for quote in ("USDT", "USDC", "BUSD", "FDUSD"):
        if symbol.endswith(quote):
            return symbol[:-len(quote)]
    return symbol


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

            if spread > min_spread:
                # We get a basic coin for searching networks
                asset = extract_asset(symbol)
                # We take nets from the cache for the base coin
                nets = NETWORK_CACHE.get(asset, [])

                print(
                    f"{symbol} | {side} | Spread: {spread:.4f}%\n"
                    f"Binance: {prices['Binance']['bid']} / {prices['Binance']['ask']}\n"
                    f"Bybit:   {prices['Bybit']['bid']} / {prices['Bybit']['ask']}\n"
                    f"Bitget:  {prices['Bitget']['bid']} / {prices['Bitget']['ask']}\n"
                )

                if not nets:
                    print("Error, network not found!")
                else:
                    print('Networks: ')
                    for n in nets:
                        print(
                            f"  - {n.network} ({n.network_name}) | "
                            f"fee={n.withdraw_fee} | "
                            f"min={n.withdraw_min} | "
                            f"time={n.transfer_time_sec}s | "
                            f"withdraw={n.withdraw_enabled} | "
                            f"deposit={n.deposit_enabled}"
                        )
                print(f"{'=' * 60}")

        time.sleep(7)

except KeyboardInterrupt:
    print("Program ended!")








from data_check import get_price_binance, get_price_bybit


# def best_exchange():
#     return get_price_binance("BTCUSDT")


prices = {
    'Binance': get_price_binance,
    'Bybit': get_price_bybit,
}

# print(best_exchange())

print(prices['Binance']('BTCUSDT'), prices['Bybit']('BTCUSDT'))


# profit = spread - buy_fees - sell_fees - withdrawal_fees







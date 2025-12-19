from data_check import get_price_binance


def best_exchange():
    return get_price_binance("BTCUSDT")


print(best_exchange())


# profit = spread - buy_fees - sell_fees - withdrawal_fees







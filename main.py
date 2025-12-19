from data_check import get_price


def best_exchange():
    return get_price("BTCUSDT")


print(best_exchange())


# profit = spread - buy_fees - sell_fees - withdrawal_fees







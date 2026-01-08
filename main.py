from data_check import get_price_binance, get_price_bybit


prices = {
    'Binance': get_price_binance,
    'Bybit': get_price_bybit,
}

data_binance = list(prices['Binance']('BTCUSDT'))
data_bybit = list(prices['Bybit']('BTCUSDT'))

price_binance_bid, price_binance_ask = float(data_binance[2]), float(data_binance[1])
price_bybit_bid, price_bybit_ask = float(data_bybit[1]), float(data_bybit[2])


def calc_bid(firstCurrency, secondCurrency):
    if firstCurrency > secondCurrency:
        result = firstCurrency - secondCurrency
        return result
    if secondCurrency > firstCurrency:
        result = secondCurrency - firstCurrency
        return result


def calc_ask(firstCurrency, secondCurrency):
    if firstCurrency > secondCurrency:
        result = firstCurrency - secondCurrency
        return result
    if secondCurrency > firstCurrency:
        result = secondCurrency - firstCurrency
        return result


def calc_spread(binance_bid, bybit_bid, binance_ask, bybit_ask):
    if binance_bid > bybit_bid:
        print('buy BTC Bybit')
        spread = ((binance_ask - bybit_bid) / binance_ask)
        return print(f'Spread is {spread:.9%}')
    if bybit_bid > binance_bid:
        print('buy BTC Binance')
        spread = ((bybit_ask - binance_bid) / bybit_ask)
        return print(f'Spread is {spread:.9%}')



calc_spread(price_binance_bid, price_bybit_bid, price_binance_ask, price_bybit_ask)
print(prices['Binance']('BTCUSDT'), prices['Bybit']('BTCUSDT'))









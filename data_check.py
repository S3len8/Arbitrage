from binance.client import Client

binance_client = Client()  # для публічних даних API ключі не потрібні
#
# # client = Client(api_key='', api_secret='')
#
# tickers = client.get_all_tickers()
# exchange_info = client.get_exchange_info()
#
# # словник тільки USDT пар
# USDT_PRICES = {
#     p['symbol']: float(p['price'])
#     for p in tickers
#     if p['symbol'].endswith('USDT')
# }
#
# # value_usdt = USDT_PRICES.get('key')
#


def get_price(symbol: str):
    data = binance_client.get_symbol_ticker(symbol=symbol)
    return float(data['price'])


prices = {
    'Binance': get_price,
    'Bybit': '',
}

# Fees for binance, bybit and others cryptocurrency exchange
# fees = {
#     'Binance': '0.01',
#     'Bybit': '0.01',
# }

print(prices['Binance']('BTCUSDT'))
#
# print(get_price("BTCUSDT"))
#
# print(USDT_PRICES)
#
# # print(value_usdt)
#
# # print(tickers)
#
#
#
#

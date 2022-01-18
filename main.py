'''
This code is written by Yan Miller
The main idea is a building Ethereum price graphic
'''

import mplfinance as mpf
import pandas as pd
import requests

def crypto_graphic(start_time, base_currency, vs_currency, interval):
    '''
    A function which creates Ethereum price graphic
    '''
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    '''
    url from binance api
    '''
    payload = {'interval': interval, 'baseTradingSymbol': base_currency, 'quoteTradingSymbol': vs_currency, 'start_time': start_time}
    response = requests.get(url, params=payload)
    data = response.json()

    open_price, close_price, high_price, low_price, time_price = [], [], [], [], []
    for candle in data:
        '''
        For loop in order to append data to our pricing lists
        '''
        open_price.append(float(candle['open']))
        high_price.append(float(candle['high']))
        low_price.append(float(candle['low']))
        close_price.append(float(candle['close']))
        time_price.append(candle['time'])

    raw_data = {
        'Date': pd.DatetimeIndex(time_price),
        'Open': open_price,
        'High': high_price,
        'Low': low_price,
        'Close': close_price
    }
    '''
    Data for building a graphic
    '''

    df = pd.DataFrame(raw_data).set_index('Date')
    '''
    variable "df" is a data frame
    '''
    print(df)
    '''
    You can show "df" in console using print, but it's not  necessary
    '''

    mpf.plot(df, type='candle', style='charles', title=base_currency, ylabel=f'Price in {vs_currency}')
    '''
    Using lib "mpf" we set technical parameters of Ethereum graphic
    '''
    mpf.show()
    return df

crypto_graphic(start_time= '2022-01-10', base_currency= 'ETH', vs_currency= 'USDT', interval='1h')
'''
You can choose any start_time, base_currency, vs_currency and interval
'''
"""
script that downloads the daily price data from bitfinex via quandl and
converts them to csv files
"""


import quandl
import pandas as pd
import os

def run():
    file = open('C:/Users/20115619/quandlKey.txt', “r”)
    authtoken = file.read()


    df = quandl.get("BITFINEX/BTCUSD", authtoken)
    df.to_csv('C:/Users/20115619/data2/BTCUSD.csv')
    print(df.tail())

    df2 = quandl.get("BITFINEX/ETHUSD", authtoken)
    df2.to_csv('C:/Users/20115619/data2/ETHUSD.csv')
    print(df2.tail())

    df3 = quandl.get("BITFINEX/IOTUSD", authtoken)
    df3.to_csv('C:/Users/20115619/data2/IOTUSD.csv')
    print(df3.tail())

    df4 = quandl.get("BITFINEX/XRPUSD", authtoken)
    df4.to_csv('C:/Users/20115619/data2/XRPUSD.csv')

    df5 = quandl.get("BITFINEX/DSHUSD", authtoken)
    df5.to_csv('C:/Users/20115619/data2/DSHUSD.csv')

    df6 = quandl.get("BITFINEX/XMRUSD", authtoken)
    df6.to_csv('C:/Users/20115619/data2/XMRUSD.csv')

    df7 = quandl.get("BITFINEX/LTCUSD", authtoken)
    df7.to_csv('C:/Users/20115619/data2/LTCUSD.csv')

if __name__ == '__main__':
    run()

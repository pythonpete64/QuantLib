"""
scatter plot
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data, compute_daily_returns


def run():

    # get data
    dates = pd.date_range('2017-06-01', '2018-06-14')
    symbols = ['BTCUSD', 'ETHUSD', 'LTCUSD','DSHUSD']
    df = get_data(symbols, dates)

    # some of the fields have NA values for now ill just drop them but this
    # is not a robust solution as i dont even know where they are in the data
    # set
    # TODO: FIX
    df = pd.DataFrame.dropna(df)

    # compute_daily_returns
    dr = compute_daily_returns(df)

    tickers = list(df.columns.values)
    print(tickers)


    # plot scatter plots for all VS BTCUSD and then fit a polynomial
    # to the data [f(y)=Mx + B]
    dr.plot(kind='scatter', grid=True, x='BTCUSD', y='LTCUSD')
    beta_LTCUSD, alpha_LTCUSD = np.polyfit(dr['BTCUSD'], dr['LTCUSD'], 1)
    plt.plot(dr['BTCUSD'], (dr['BTCUSD']*beta_LTCUSD) + alpha_LTCUSD,
             '-', color='r')

    dr.plot(kind='scatter', grid=True, x='BTCUSD', y='ETHUSD')
    beta_ETHUSD, alpha_ETHUSD = np.polyfit(dr['BTCUSD'], dr['ETHUSD'], 1)
    plt.plot(dr['BTCUSD'], (dr['BTCUSD']*beta_ETHUSD) + alpha_ETHUSD,
             '-', color='r')

    dr.plot(kind='scatter', grid=True, x='BTCUSD', y='DSHUSD')
    beta_DSHUSD, alpha_DSHUSD = np.polyfit(dr['BTCUSD'], dr['DSHUSD'], 1)
    plt.plot(dr['BTCUSD'], (dr['BTCUSD']*beta_DSHUSD) + alpha_DSHUSD,
             '-', color='r')

    print('-'*20)
    print("ETHUSD Alpha: " +str(alpha_ETHUSD))
    print("LTCUSD Alpha: " +str(alpha_LTCUSD))
    print("DSHUSD Alpha: " +str(alpha_DSHUSD))
    print('-'*20)
    print("ETHUSD Beta: " +str(beta_ETHUSD))
    print("LTCUSD Beta: " +str(beta_LTCUSD))
    print("DSHUSD Beta: " +str(beta_DSHUSD))
    print('-'*20)
    print('Daily Returns Corrilations: ')
    print(dr.corr(method='pearson'))

    plt.show()





if __name__ == '__main__':
    run()

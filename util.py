"""
Uitlity functions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# returns a path for a cymbol
def symbol_to_path(symbol, base_dir='data'):
    return os.path.join(base_dir, '{}.csv'.format(str(symbol)))

# gets close data for symbols for the dates passed as a dataframe
def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Last'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Last': symbol})
        df = df.join(df_temp)

    return df

# normalises the data
def normalise_data(_df):
    return _df / _df.ix[0, :]

# Compute and return the daily return values.
def compute_daily_returns(df):
    daily_returns = (df / df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns

# plot asset prices
def plot_data(_df, _title="Crypto-Assets"):
    ax = _df.plot(title = _title, fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

# plot daily returns as a histogram, method also calculates
# and prints out the mean standard deviation and kurtosis
# only takes one ticker at a time
def plot_daily_returns_hist(_df, _bins=20):
    dailyReturns = compute_daily_returns(_df)
    dailyReturns.hist(bins=_bins)

    mean = dailyReturns.mean()
    std = dailyReturns.std()
    kurtosis = dailyReturns.kurtosis()

    plt.axvline(float(mean), color='w', linestyle='dashed', linewidth=2)
    plt.axvline(float(std), color='r', linestyle='dashed', linewidth=2)
    plt.axvline(float(-std), color='r', linestyle='dashed', linewidth=2)
    plt.show()

    print('-'*20)
    print(dailyReturns.mean().to_string().split(' ', 1)[0])
    print('-'*20)
    print("Mean:"+ dailyReturns.mean().to_string().split(' ', 1)[1])
    print("standard dev:"+ dailyReturns.std().to_string().split(' ', 1)[1])
    print("kurtosis:"+ dailyReturns.kurtosis().to_string().split(' ', 1)[1])


# the first column in the DF is the benchmark
def scatter_abc(_df):
    # some of the fields have NA values for now ill just drop them but this
    # is not a robust solution as i dont even know where they are in the data
    # set
    # TODO: unit tests on this. i dont think its giving accurate results

    tickers = list(_df.columns.values)
    xTick=str(tickers[0])
    yTick=str(tickers[1])
    print(tickers)
    df = pd.DataFrame.dropna(_df)
    # compute_daily_returns
    dr = compute_daily_returns(df)

    # plot scatter plots for first VS second and then fit a polynomial
    # to the data [f(y)=Mx + B]
    dr.plot(kind='scatter', grid=True, x= str(tickers[0]), y=str(tickers[1]))
    beta, alpha = np.polyfit(dr[tickers[0]], dr[tickers[1]], 1)
    plt.plot(dr[xTick], (dr[xTick]*beta) + alpha, '-', color='r')

    # print stats
    print('-'*20)
    print(yTick +" Alpha: " +str(alpha))
    print(yTick +" Beta: " +str(beta))
    print('Daily Returns Corrilations: ')
    print(dr.corr(method='pearson'))
    print('-'*20)


    plt.show()


# plot selected asset prices
def plot_selected(_df, columns, start_index, end_index):
    plot_data(_df.ix[start_index:end_index, columns])

def test_run():
    dates = pd.date_range('2017-01-01', '2018-06-01')
    symbols = ['BTCUSD', 'LTCUSD']
    df1 = get_data(symbols, dates)

    scatter_abc(df1)




if __name__ == "__main__":
    test_run()

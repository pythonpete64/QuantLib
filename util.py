"""
Uitlity functions
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

""" returns a path for a cymbol"""
def symbol_to_path(symbol, base_dir='data'):
    return os.path.join(base_dir, '{}.csv'.format(str(symbol)))

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

def normalise_data(_df):
    return _df / _df.ix[0, :]

"""Compute and return the daily return values."""
def compute_daily_returns(df):
    daily_returns = (df / df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns

"""plot asset prices"""
def plot_data(_df, _title="Crypto-Assets"):
    ax = _df.plot(title = _title, fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

"""plot selected asset prices"""
def plot_selected(_df, columns, start_index, end_index):
    plot_data(_df.ix[start_index:end_index, columns])

def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-06-01')

    # Choose symbols to read
    symbols = ['BTCUSD', 'ETHUSD', 'LTCUSD']

    # Get stock data
    df = get_data(symbols, dates)

    normalsed = normalise_data(df)
    plot_data(df, "Crypto-Assets")
    plot_data(normalsed, "Crypto-Assets Normalised")
    plot_data(compute_daily_returns(df), "Crypto-Assets Daily Returns")

    print(df)


if __name__ == "__main__":
    test_run()

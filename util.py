"""
Uitlity functions
"""

import pandas as pd
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

def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-06-01')

    # Choose symbols to read
    symbols = ['BTCUSD', 'ETHUSD', 'LTCUSD']

    # Get stock data
    df = get_data(symbols, dates)
    print(df)


if __name__ == "__main__":
    test_run()

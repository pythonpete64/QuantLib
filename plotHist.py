import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns

def run():
    """read data"""
    dates = pd.date_range('2016-01-01', '2018-06-01')
    symbols = ['BTCUSD']
    df = get_data(symbols, dates)
    plot_data(df, "Bitcoin price")

    """compute daily returns"""
    dailyReturns = compute_daily_returns(df)
    plot_data(dailyReturns, "Bitcoin Daily Returns")

    dailyReturns.hist(bins=80)
    plt.show()

    mean = dailyReturns.mean()
    print("Mean: "+str(mean))
    std = dailyReturns.std()
    print("standard dev : "+str(std))




if __name__ == '__main__':
    run()

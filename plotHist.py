import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns

def run():
    """read data"""
    dates = pd.date_range('2016-01-01', '2018-06-01')
    symbols = ['ETHUSD']
    df = get_data(symbols, dates)

    """compute daily returns"""
    dailyReturns = compute_daily_returns(df)
    dailyReturns.hist(bins=20)

    mean = dailyReturns.mean()
    std = dailyReturns.std()
    kurtosis = dailyReturns.kurtosis()
    print("Mean:"+ dailyReturns.mean().to_string().split(' ', 1)[1])
    print("standard dev:"+ dailyReturns.std().to_string().split(' ', 1)[1])
    print("kurtosis:"+ dailyReturns.kurtosis().to_string().split(' ', 1)[1])


    plt.axvline(float(mean), color='w', linestyle='dashed', linewidth=2)
    plt.axvline(float(std), color='r', linestyle='dashed', linewidth=2)
    plt.axvline(float(-std), color='r', linestyle='dashed', linewidth=2)
    plt.show()




if __name__ == '__main__':
    run()

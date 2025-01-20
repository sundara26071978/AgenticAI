
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def compute_var_ratio(returns):
    n = len(returns)
    var_ratio = np.zeros((n - 1,))
    for t in range(1, n):
        var_ratio[t-1] = np.mean((returns[t-1])/(returns[:t-1])) / np.mean((returns[:t-1])/returns[:t-1])
    return var_ratio

ticker = 'IONQ'
start_date = '2024-01-01'
end_date = '2024-12-31'
data = yf.download(ticker, start=start_date, end=end_date)['Adj Close'].pct_change()

returns = data.dropna()

var_ratio = compute_var_ratio(returns)

plt.plot(var_ratio)
plt.title('Variance Ratio for ' + ticker)
plt.xlabel('Time')
plt.ylabel('Variance Ratio')
plt.show()

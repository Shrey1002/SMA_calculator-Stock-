import pandas_datareader as pdr
import datetime as dt
ticker = "RELIANCE.NS"
start = dt.datetime(2021, 1, 1)
end = dt.datetime(2022, 1, 1)
data = pdr.get_data_yahoo(ticker, start, end)
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()
data.to_excel("final_output.xlsx")
print(data.head())
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

stock = input('Type in the stock do you want to monitor: ')
start_date = input('Type in the start date YYYY-MM-DD: ')
end_date = input('Type in the end date YYYY-MM-DD: ')

# Download TSLA stock data
data = yf.download(stock, start=start_date, end=end_date)

# Calculate moving averages
data['50_day_MA'] = data['Close'].rolling(window=50).mean()
data['20_day_MA'] = data['Close'].rolling(window=20).mean()
data['20_day_std'] = data['Close'].rolling(window=20).std()
data['Upper_Band'] = data['20_day_MA'] + (2 * data['20_day_std'])
data['Lower_Band'] = data['20_day_MA'] - (2 * data['20_day_std'])

# Plot stock price and moving averages
fig, axes = plt.subplots(figsize=(12,6))
axes.plot(data['Close'], label='Close')
axes.plot(data['50_day_MA'], 'r', label='50 Day MA')

axes.set_xlim(pd.Timestamp(start_date), pd.Timestamp(end_date))
axes.set_ylim(0, int(round(data['Close'].max())))
axes.set_title('{} Stock Price and Moving Averages'.format(stock))
axes.set_xlabel('Date')
axes.set_ylabel('Price (USD)')

# Plot Bollinger Bands
axes.plot(data['Upper_Band'], '--', label='Upper Bollinger Band')
axes.plot(data['Lower_Band'], color='brown', linestyle='-.', label='Lower Bollinger Band')

# Save the figure
fig.savefig('{}_Stock_Price_and_Moving_Averages_Line_Chart.png'.format(stock))

# Show the legend
axes.legend()

# Resample data to yearly frequency and handle MultiIndex columns
data.columns = [col[0] for col in data.columns]  # Flatten MultiIndex columns
yearly_data = data.resample('YE').ohlc()  # Resample data to yearly frequency

# Flatten MultiIndex columns for yearly data
yearly_data.columns = ['_'.join(col) for col in yearly_data.columns]

# Rename columns to match mplfinance's expectations
yearly_data.rename(columns={
    'Open_open': 'Open',
    'High_high': 'High',
    'Low_low': 'Low',
    'Close_close': 'Close',
    'Volume_open': 'Volume'
}, inplace=True)

# Plot the yearly candlestick chart
mpf.plot(
    yearly_data,
    type='candle',
    style='yahoo',
    title='{} Yearly Candlestick Chart'.format(stock),
    figsize=(12, 6))


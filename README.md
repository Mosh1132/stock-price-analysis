# Stock Price Analysis and Visualization

This Python project allows users to analyze stock price data, calculate moving averages, and visualize the data using various charts. It fetches stock data using the `yfinance` library, calculates Bollinger Bands, and generates moving average and candlestick charts using `matplotlib` and `mplfinance`.

## Features

- **Stock Data Download:** Uses `yfinance` to download historical stock data.
- **Moving Averages:** Calculates 50-day and 20-day moving averages.
- **Bollinger Bands:** Calculates and plots the upper and lower Bollinger Bands.
- **Visualizations:** Plots stock prices, moving averages, and Bollinger Bands using `matplotlib`.
- **Candlestick Chart:** Generates yearly candlestick charts using `mplfinance`.

## Requirements

To run the script, you need the following Python libraries:

- `yfinance`
- `matplotlib`
- `pandas`
- `mplfinance`

You can install them via pip:

```bash
pip install yfinance matplotlib pandas mplfinance

import yfinance as yf

# Fetch 1-minute interval data for the last day
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1d", interval="1m")
print(data)

import yfinance as yf
import pandas as pd

# Step 1: Get the list of S&P 500 stock tickers
def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    df = table[0]  # The first table contains the ticker symbols
    return df['Symbol'].tolist()

# Step 2: Function to check if a stock has dropped more than 5%
def check_stock_drop(ticker):
    stock = yf.Ticker(ticker)

    # Get the data for the past 5 days (to ensure we have 2 days' worth of data)
    hist = stock.history(period="5d", interval="1d")

    if len(hist) >= 2:
        # Use .iloc to access values by position, avoiding future warnings
        previous_close = hist['Close'].iloc[-2]  # Closing price of the previous day
        current_price = hist['Close'].iloc[-1]   # Closing price of the current day

        # Calculate the percentage drop from the previous day
        percent_drop = ((previous_close - current_price) / previous_close) * 100
        return percent_drop
    else:
        return None

# Step 3: Main function to run the script
def find_stocks_dropping_5_percent():
    tickers = get_sp500_tickers()

    # Loop through each stock ticker in the S&P 500
    for ticker in tickers:
        try:
            percent_drop = check_stock_drop(ticker)
            if percent_drop is not None and percent_drop > 5:
                print(f"{ticker} has dropped by {percent_drop:.2f}% today!")
        except Exception as e:
            print(f"Error checking {ticker}: {e}")

# Step 4: Run the script
if __name__ == "__main__":
    find_stocks_dropping_5_percent()

import sys
import yfinance as yf

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.fast_info["lastPrice"]
        print(f"The current price of {ticker} is ${price:.2f}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

if __name__ == "__main__":
    ticker = sys.argv[-1] if len(sys.argv) > 1 else "WDC"
    get_stock_price(ticker)

# src/fetch_stock.py

import yfinance as yf
import pandas as pd

def fetch_apple_stock_data(start: str = "2020-01-01", end: str = None) -> pd.DataFrame:
    """
    Fetch historical stock data for Apple (AAPL).

    Parameters:
    - start (str): Start date in 'YYYY-MM-DD' format.
    - end (str, optional): End date in 'YYYY-MM-DD' format. If None, uses today.

    Returns:
    - pd.DataFrame: DataFrame containing historical Apple stock data.
    """
    apple = yf.Ticker("AAPL")
    hist = apple.history(start=start, end=end)
    return hist

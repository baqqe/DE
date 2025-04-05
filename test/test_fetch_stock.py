# test/test_fetch_stock.py

from src.fetch_stock import fetch_apple_stock_data

def test_fetch_apple_stock_data():
    df = fetch_apple_stock_data("2023-01-01", "2023-01-10")
    assert not df.empty
    assert "Close" in df.columns

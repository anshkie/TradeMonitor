import yfinance as yf
from datetime import datetime, timedelta

# Get live price from Yahoo
def get_ltp(symbol):
    data = yf.Ticker(symbol)
    hist = data.history(period="1d", interval="1m")
    if not hist.empty:
        return round(hist['Close'].iloc[-1], 2)
    return None

# Updated mock positions
def get_mock_positions():
    symbols = [
        {"symbol": "RELIANCE.NS", "qty": 10, "entry_price": 2400},
        {"symbol": "TCS.NS", "qty": -5, "entry_price": 3500},
        {"symbol": "INFY.NS", "qty": 15, "entry_price": 1400},
        {"symbol": "HDFCBANK.NS", "qty": 20, "entry_price": 1600},
        {"symbol": "ICICIBANK.NS", "qty": -10, "entry_price": 950},
        {"symbol": "SBIN.NS", "qty": 25, "entry_price": 580},
        {"symbol": "AXISBANK.NS", "qty": -8, "entry_price": 970},
    ]

    for stock in symbols:
        stock["ltp"] = get_ltp(stock["symbol"])
    return symbols

# Updated mock orders
def get_mock_orders():
    now = datetime.now()
    return [
        {"symbol": "RELIANCE", "action": "BUY", "price": 2400, "qty": 10, "timestamp": now - timedelta(minutes=30)},
        {"symbol": "TCS", "action": "SELL", "price": 3500, "qty": 5, "timestamp": now - timedelta(minutes=15)},
        {"symbol": "INFY", "action": "BUY", "price": 1400, "qty": 15, "timestamp": now - timedelta(hours=1)},
        {"symbol": "HDFCBANK", "action": "BUY", "price": 1600, "qty": 20, "timestamp": now - timedelta(minutes=90)},
        {"symbol": "ICICIBANK", "action": "SELL", "price": 950, "qty": 10, "timestamp": now - timedelta(minutes=45)},
        {"symbol": "SBIN", "action": "BUY", "price": 580, "qty": 25, "timestamp": now - timedelta(minutes=20)},
        {"symbol": "AXISBANK", "action": "SELL", "price": 970, "qty": 8, "timestamp": now - timedelta(minutes=10)},
    ]

# 📊 Trade Monitor App

A lightweight trading monitor dashboard built in Python that tracks mock or live stock positions and orders. It’s designed to fetch market data and simulate a basic trading system interface — perfect for backtesting, strategy visualization, and prototyping real-time trading systems.

LIVE URL : https://trademonitor-safpfmg3eftf3vqfv7htzg.streamlit.app/
---

## 🔧 Features

- ✅ Live price fetching using `yfinance`
- 📈 Display of current mock positions with real-time LTP
- 🧾 Recent order list with timestamp and details
- 💡 Modular code structure for easy updates or real API integration
- 🌐 Streamlit-ready interface for fast UI deployment (if using it)

---

## 📁 Project Structure

```
TESTNG/
│
├── app.py               # Main dashboard application
├── mock_data.py         # Mock positions and orders with live prices
├── utils.py             # Utility functions (extendable)
├── requirements.txt     # Python dependencies
├── venv/                # Virtual environment (should be gitignored)
└── __pycache__/         # Compiled cache (should be gitignored)
```

---

## 🚀 How to Run

1. **Clone the repo:**
   ```bash
   https://github.com/anshkie/TradeMonitor.git
   cd trade-monitor-app
   ```

2. **Create and activate virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app (example with Streamlit):**
   ```bash
   streamlit run app.py
   ```

---

## 📌 Future Enhancements

- 🔄 Integration with real broker APIs (AngelOne, Zerodha)
- 🧠 Strategy backtesting module
- 📊 Performance tracking dashboard
- 🗄️ Database support for historical order tracking

---

## 🧠 Skills Demonstrated

- Python (Data handling, modular code)
- API integration (`yfinance`, ready for broker APIs)
- Trading domain concepts (positions, orders, LTP)
- Streamlit UI development (if used)
- Environment setup & version control (venv, `.gitignore`, `requirements.txt`)

---

## 📬 Contact

Feel free to reach out if you'd like to collaborate or need help integrating live trading APIs!

**Ansh Gupta**  
📧 anshnew41@gmail.com  

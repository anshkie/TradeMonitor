import streamlit as st
from mock_data import get_mock_positions, get_mock_orders
from utils import calculate_pnl
import pandas as pd

st.set_page_config(page_title="Trade Monitor Dashboard", layout="wide")

st.title("Trade Monitoring Dashboard")

# --- Open Positions ---
st.header("Open Positions")
positions = get_mock_positions()

for pos in positions:
    pos['P&L'] = calculate_pnl(pos)

df_positions = pd.DataFrame(positions)
df_positions["symbol"] = df_positions["symbol"].str.replace(".NS", "", regex=False)
st.dataframe(df_positions, use_container_width=True)

# --- Order History ---
st.header("Order History")
orders = get_mock_orders()

for order in orders:
    order['timestamp'] = order['timestamp'].strftime("%Y-%m-%d %H:%M:%S")

df_orders = pd.DataFrame(orders)
st.dataframe(df_orders, use_container_width=True)

# --- Summary Metrics ---
st.header("Summary")
total_pnl = sum([p["P&L"] for p in positions])
st.metric("Total P&L", f"₹{total_pnl}")

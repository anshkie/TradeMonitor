def calculate_pnl(position):
    if position["ltp"] is None:
        return 0.0
    return round((position["ltp"] - position["entry_price"]) * position["qty"], 2)

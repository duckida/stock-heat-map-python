# stock-heat-map-python
Python Turtle heatmap for S&amp;P 500 stocks

<img width="838" height="173" alt="Screenshot 2026-02-21 at 5 44 26 PM" src="https://github.com/user-attachments/assets/6dae6bc0-2c72-4e0c-8737-f8ceb29b0929" />

There are 2 APIs used - you can choose one that you like! Neither need API keys:
- Yahoo Finance `yfinance` - highly rate limited
- `stock-prices.on99.app/quotes` - web-based request API

Ensure you have Turtle installed to run the app! The stock information updates every 2 seconds and refreshes the heatmap.

### Installation instructions:
1. Clone the repo: `https://github.com/duckida/stock-heat-map-python && cd stock-heat-map-python`
2. Install dependencies: `uv sync`
3. Run the app: `uv run main.py`

OR use `pipx`: `pipx install git+https://github.com/duckida/stock-heat-map-python.git`

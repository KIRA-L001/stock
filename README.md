# 📈 Stock Forecast App

An interactive stock price forecasting web app built with **Streamlit**, **yfinance**, **Prophet**, and **Plotly**.

Select a ticker, choose a forecast horizon (1–4 years), and get an interactive time-series forecast with trend and seasonality components.

## Features

- 📊 Historical price data pulled live from Yahoo Finance (since 2015)
- 🔮 Time-series forecasting with Facebook Prophet
- 🖱️ Interactive Plotly charts with range slider
- 🎛️ Simple ticker selector (GOOG, AAPL, MSFT, GME) and prediction-horizon slider
- 🌒 Dark gradient themed UI

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/KIRA-L001/stock.git
cd stock
pip install -r requirements.txt
```

### Run

```bash
streamlit run main.py
```

Then open the URL Streamlit prints (usually http://localhost:8501).

## How It Works

1. Downloads OHLC data for the selected ticker via `yfinance`.
2. Plots raw open/close prices with an interactive range slider.
3. Trains a Prophet model on closing prices.
4. Forecasts up to 4 years ahead and renders the forecast plus its components (trend, weekly/yearly seasonality).

## License

MIT — see [LICENSE](LICENSE).

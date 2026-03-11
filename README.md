# 📈 StockIQ — Stock Market Intelligence Dashboard

A real-time stock market analysis dashboard built with **FastAPI + Python**, featuring algorithmic moving average crossover signals and an interactive price chart UI.

🔗 **Live Demo:** https://stock-dashboard-ibnb.onrender.com

---

## Features

- 🔴 **Live Stock Prices** — Real-time data fetched via Yahoo Finance API
- 📊 **Interactive Price Charts** — 3-month historical price visualization
- 🤖 **MA Crossover Signal** — Algorithmic BUY/SELL signals using 20-day vs 50-day moving averages
- ⚡ **Quick Search** — One-click analysis for AAPL, TSLA, MSFT, GOOGL, NVDA, JPM
- 🎨 **Modern UI** — Glassmorphism design with animated gradients

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| Data | yfinance, pandas |
| Frontend | HTML, CSS, Chart.js |
| Deployment | Render |

---

## How It Works

1. User enters a stock ticker (e.g. AAPL)
2. FastAPI backend calls yfinance to fetch 3 months of price data
3. pandas computes 20-day and 50-day moving averages
4. If MA20 > MA50 → **BUY** signal (bullish momentum)
5. If MA20 < MA50 → **SELL** signal (bearish momentum)
6. Chart.js renders the price chart in real time

---

## Run Locally
```bash
git clone https://github.com/lakshgupta260-dev/stock-dashboard.git
cd stock-dashboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000`

---

## Author

**Laksh Gupta** — B.Tech CSE, Manipal University Jaipur  
📧 lakshgupta260@gmail.com
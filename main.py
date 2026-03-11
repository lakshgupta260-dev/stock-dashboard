from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import yfinance as yf
import pandas as pd

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/stock/{symbol}")
async def get_stock(symbol: str):
    ticker = yf.Ticker(symbol.upper())
    df = ticker.history(period="3mo")
    
    if df.empty:
        return {"error": "Invalid symbol"}
    
    # Calculate moving averages
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()
    
    # Trading signal
    last = df.iloc[-1]
    signal = "BUY" if last["MA20"] > last["MA50"] else "SELL"
    
    prices = df["Close"].round(2).tolist()
    dates = df.index.strftime("%Y-%m-%d").tolist()
    
    return {
        "symbol": symbol.upper(),
        "current_price": round(last["Close"], 2),
        "signal": signal,
        "ma20": round(last["MA20"], 2),
        "ma50": round(last["MA50"], 2),
        "prices": prices,
        "dates": dates,
    }
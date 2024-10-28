import yfinance as yf
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

#setting up the database
db = pymysql.connect(host = "localhost", user = "root", password = "password", database = "portfolio_management")
cursor = db.cursor()

#brand tickers and ids
brands = {
    'NKE' : 1,
    'LVMUY': 2,     # LVMH
    'ADDYY': 3,     # Adidas
    'ITX.MC': 4,    # Inditex
    'HNNMY': 5,     # H&M
    'CPRI': 6,      # Capri Holdings
    'RL': 7         # Ralph Lauren
}

#fetch data
for ticker, id in brands.items():
    stock = yf.Ticker(ticker)
    history = stock.history(period='1y')
    #insert data
    for date, row in history.iterrows():
        cursor.execute("""
                INSERT INTO historical_prices (asset_id, date, open_price, close_price, volume)
                VALUES (%s, %s, %s, %s, %s)
            """, (id, date.date(), row['Open'], row['Close'], row['Volume']))
    db.commit()
db.close()






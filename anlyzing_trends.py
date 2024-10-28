import pymysql
import pandas as pd
import matplotlib.pyplot as plt

db = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="portfolio_management"
)


company_names = {
    1: "Nike (NKE)",
    2: "LVMH (LVMUY)",
    3: "Adidas (ADDYY)",
    4: "Inditex (ITX.MC)",
    5: "H&M (HNNMY)",
    7: "Ralph Lauren (RL)"
}

for id, name in company_names.items():
    # Query data for a specific asset 
    query = f"""
    SELECT date, close_price
    FROM historical_prices
    WHERE asset_id = {id}
    ORDER BY date;
    """
    df = pd.read_sql(query, db)

    # daily percentage change
    df['pct_change'] = df['close_price'].pct_change() * 100

    # Plot closing price and percentage change
    fig, ax1 = plt.subplots()

    # Plot closing price
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Closing Price', color='blue')
    ax1.plot(df['date'], df['close_price'], color='blue', label="Closing Price")
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a second y-axis for percentage change
    ax2 = ax1.twinx()
    ax2.set_ylabel('Percentage Change', color='red')
    ax2.plot(df['date'], df['pct_change'], color='red', linestyle='--', label="Daily % Change")
    ax2.tick_params(axis='y', labelcolor='red')

    fig.tight_layout()
    plt.title(f" {name}: Closing Price and Daily Percentage Change")
    plt.show()
db.close()
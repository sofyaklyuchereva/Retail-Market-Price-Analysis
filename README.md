# Retail Market Price Analysis
This project provides an in-depth analysis of historical price trends for retail market assets. The primary focus is on descriptive analytics to reveal seasonal patterns, peak periods, and price change trends. Predictive modeling was attempted but proved challenging due to irregular patterns in the data.

## Project Overview
The project includes:
1. SQL Database Setup: Data was stored in an SQL database for efficient querying and structured analysis.
2. Exploratory Data Analysis (EDA): Historical data was explored to uncover trends, seasonality, and key patterns.

## Contents 
- Data: Stored in an SQL database with tables for assets, historical prices, portfolio, transactions, and users.
- Scripts:
  - loading_data.py: Script for loading data into the SQL database.
  - analyzing_trends.py: Script for analyzing trends and generating descriptive insights.
- Visualization: Created using Tableau and Python, with images to illustrate key trends.
- README.md: Documentation for the project.

## Analysis and Visualization
### Asset Closing Price and Weekly Moving Average Over Time
This visualization shows the trend of closing prices alongside the weekly moving average for various assets over the course of a year. Each asset is represented by a unique color, with solid lines indicating the actual closing prices and dotted lines representing the weekly moving average.

**Insights**:
- There is a consistent upward trend in closing prices for most assets, indicating potential growth in value over time.
- The weekly moving average smooths out short-term fluctuations and provides a clearer view of the underlying trend.
- Assets show different growth trajectories, with some having steeper increases, indicating faster growth.

### Price Change During Each Month with Trend Line
This bar chart displays monthly price changes, categorized by positive (green) and negative (red) changes. A trend line overlays the chart, showing a slight upward trend in price changes over the months.

**Insights**:
- Price changes vary significantly by month, with some months experiencing high positive or negative changes.
- October and November show larger positive and negative changes, respectively, potentially indicating a seasonal impact.
- The trend line suggests a slight increase in overall price changes, but the fluctuations imply external market influences affecting retail prices month-to-month.

### Closing Price and Daily Percentage Change
These chart show the closing price (in blue) and daily percentage change (in red, dashed line) for all brands over a period of one year. This visualization provides a dual-axis view, with price on the left and percentage change on the right.

## How to run this project
1. Install dependencies
2. Set up an SQL database
   - Use loading_data.py to load data into the SQL database.
   - Connect to the database and verify the tables using SQL queries or DB management tools.
3. Run Data Analysis
4. Visualizations
   - Visualization files (created in Tableau and Python) illustrate key trends and are saved in the data folder.

## Results and key findings
- **Seasonal Patterns:** Observed consistent weekly and monthly trends for various assets.
- **Price Fluctuations:** Certain assets experience more volatility, with substantial monthly changes.

## Future improvements
- **Additional Data:** Incorporating external factors, such as economic indicators, may improve forecasting potential.
- **Alternative Models:** Exploring machine learning models with engineered features for short-term predictions could provide more accurate results.


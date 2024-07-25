Trading Analysis
This repository contains tools and scripts for performing trading analysis, including data cleaning, predictive modeling, and web scraping to gather relevant trading data. The project aims to help analysts and data scientists gain insights into trading patterns and develop strategies based on historical data.

#Usage
Data Extraction
The data_extraction.py script fetches 1-minute candlestick data for BTC-USD from Binance and saves it to a CSV file, which is assumed to be the data lake.

To run the data extraction script, use the following command:

bash
Copy code
python data_extraction.py
Data Storage
The extracted data is stored in a CSV file with the following columns:

Trading Pair
Open Price
Close Price
High Price
Low Price
BTC Volume
USD Volume
Number of Trades
Candle Open Time
Candle Close Time
Schema Design
Based on the raw data extracted, the schema design includes the following fact and dimension tables:

Fact Table: fact_trades
fact_id (Primary Key)
trading_pair (e.g., "BTC-USD")
open_price
close_price
high_price
low_price
btc_volume
usd_volume
number_of_trades
open_time (timestamp)
close_time (timestamp)
Dimension Table: dim_time
time_id (Primary Key)
timestamp
minute
hour
day
week
month
quarter
year
Sample Queries
1. 52 Week High and Low for All Items Traded in the Past 3 Months
2. High/Low Price/Volume in the Past 2 Hours
3. Volume for a Given Timeframe
4. Monthly, Quarterly, and Yearly Volume for Items with 10 Million+ Volume Over the Past Year

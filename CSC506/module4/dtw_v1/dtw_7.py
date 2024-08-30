# importing 'yfinance' to fetch historical stock market data for specified date-time periods
import yfinance as yf
# importing numpy for numerical computations
import numpy as np
# importing dtw library to calcilate dtw distance between 2 time series
from dtaidistance import dtw
# importing pandas for data handling
import pandas as pd
# importing plotting library
import matplotlib.pyplot as plt
# importing os module to create directories to be able to save and read files
import os

# Define the directories to save time series data and plots
output_dir = "time_series"
plots_dir = "plots"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(plots_dir, exist_ok=True)

# Define tickers
ticker_1_symbol = "TSLA"
ticker_2_symbol = "AMZN"

# Define custom start and end dates
start_date_1 = "2024-06-01"  # Start date for the first ticker
end_date_1 = "2024-08-01"    # End date for the first ticker

start_date_2 = "2024-06-01"  # Start date for the second ticker
end_date_2 = "2024-08-01"    # End date for the second ticker

# Fetching historical stock price data using the defined date range
ticker_1 = yf.Ticker(ticker_1_symbol)
ticker_2 = yf.Ticker(ticker_2_symbol)

# Get data for the specified start and end dates
data_1 = ticker_1.history(start=start_date_1, end=end_date_1)
data_2 = ticker_2.history(start=start_date_2, end=end_date_2)

# Save the data to CSV files
data_1.to_csv(os.path.join(output_dir, f"{ticker_1_symbol}_data.csv"))
data_2.to_csv(os.path.join(output_dir, f"{ticker_2_symbol}_data.csv"))

# Use the closing price for comparison
series_1 = data_1['Close'].values
series_2 = data_2['Close'].values

# Check for missing values and handle them using ffill() directly
series_1 = np.asarray(pd.Series(series_1).ffill().values, dtype=float)
series_2 = np.asarray(pd.Series(series_2).ffill().values, dtype=float)

# Ensure both series are of equal length
min_length = min(len(series_1), len(series_2))
series_1 = series_1[:min_length]
series_2 = series_2[:min_length]

# Add debugging output to check data
print(f"Series 1 length: {len(series_1)}, first few values: {series_1[:5]}")
print(f"Series 2 length: {len(series_2)}, first few values: {series_2[:5]}")

# Calculate DTW distance
distance = dtw.distance(series_1, series_2)
print(f"DTW distance between {ticker_1_symbol} and {ticker_2_symbol}: {distance}")

# Calculate cost matrix and warping paths without specifying 'use_c'
accumulated_cost, cost_matrix = dtw.warping_paths(series_1, series_2)

# Debugging: print types and values to verify output
print(f"Type of cost_matrix: {type(cost_matrix)}")
print(f"Type of accumulated_cost: {type(accumulated_cost)}")
print(f"Cost matrix: {cost_matrix}")
print(f"Accumulated cost: {accumulated_cost}")

# Plot the cost matrix
if isinstance(cost_matrix, np.ndarray) and cost_matrix.ndim == 2:
    plt.figure(figsize=(8, 6))
    plt.imshow(cost_matrix, origin='lower', cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.title("Cost Matrix")
    plt.xlabel(f"{ticker_2_symbol} Index")
    plt.ylabel(f"{ticker_1_symbol} Index")
    plt.savefig(os.path.join(plots_dir, "cost_matrix.png"))
    plt.close()
else:
    print("Cost matrix is not generated correctly or is not a 2D array. Please check the inputs and function output.")

# Visualization of time series
plt.figure(figsize=(10, 6))
plt.plot(data_1.index[:min_length], series_1, label=ticker_1_symbol, color="blue")
plt.plot(data_2.index[:min_length], series_2, label=ticker_2_symbol, color="green")
plt.title(f"Stock Price Comparison: {ticker_1_symbol} vs {ticker_2_symbol}")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.savefig(os.path.join(plots_dir, "stock_price_comparison.png"))
plt.close()

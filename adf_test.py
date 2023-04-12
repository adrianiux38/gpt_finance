import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Read the CSV file
bitcoin_data = pd.read_csv('bitcoin_prices2.csv')

# Convert the 'Date' column to datetime objects
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])

# Remove commas from the 'Price' column and convert to float
bitcoin_data['Price'] = bitcoin_data['Price'].apply(lambda x: float(x.replace(',', '')))

# Set the 'Date' column as the DataFrame index
bitcoin_data.set_index('Date', inplace=True)

# Sort the DataFrame by index (date)
bitcoin_data.sort_index(inplace=True)

# Calculate the second difference (d=2) of the Bitcoin price data
bitcoin_data['Price_diff_2'] = bitcoin_data['Price'].diff().diff()

# Drop missing values created by differencing
bitcoin_data.dropna(inplace=True)

# Perform the ADF test on the second-differenced data
adf_result = adfuller(bitcoin_data['Price_diff_2'])

# Print the ADF test results
print("ADF Statistic:", adf_result[0])
print("p-value:", adf_result[1])
print("Critical Values:")
for key, value in adf_result[4].items():
    print("\t{}: {}".format(key, value))

# Check if the ADF test suggests stationarity
if adf_result[1] < 0.05:
    print("The second-differenced data is stationary, the ARIMA(1, 2, 1) model should be appropriate.")
else:
    print("The second-differenced data is not stationary, consider using a different order for the ARIMA model.")
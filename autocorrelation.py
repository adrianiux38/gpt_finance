import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

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

# Plot the autocorrelation of the second-differenced Bitcoin price data
fig, ax = plt.subplots(figsize=(12, 6))
plot_acf(bitcoin_data['Price_diff_2'], lags=20, ax=ax)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation of Second-Differenced Bitcoin Price Data')
plt.grid()
plt.show()
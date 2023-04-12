import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf

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

# Calculate the second difference of the 'Price' column
bitcoin_data['Price_diff_2'] = bitcoin_data['Price'].diff().diff()

# Drop missing values caused by differencing
bitcoin_data.dropna(inplace=True)

# Plot the partial autocorrelation with d=2
fig, ax = plt.subplots(figsize=(12, 6))
plot_pacf(bitcoin_data['Price_diff_2'], lags=15, ax=ax, method='ywm')
plt.xlabel('Lags')
plt.ylabel('Partial Autocorrelation')
plt.title('Partial Autocorrelation with d=2')
plt.grid()
plt.show()
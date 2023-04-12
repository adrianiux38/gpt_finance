import pandas as pd
import matplotlib.pyplot as plt

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

# Calculate the first difference (d=1) of the Bitcoin price data
bitcoin_data['Price_Difference'] = bitcoin_data['Price'].diff()

# Plot the first difference of the Bitcoin price data
plt.figure(figsize=(12, 6))
plt.plot(bitcoin_data.index, bitcoin_data['Price_Difference'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price Difference')
plt.title('First Difference (d=1) of Bitcoin Price vs Date')
plt.grid()
plt.show()
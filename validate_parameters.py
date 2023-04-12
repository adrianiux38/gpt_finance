import pandas as pd
import pmdarima as pm

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

# Use auto_arima to find the optimal parameters for the ARIMA model
optimal_arima = pm.auto_arima(bitcoin_data['Price'], suppress_warnings=True, seasonal=False, stepwise=True)

# Print the optimal parameters
print("The optimal parameters for the ARIMA model are:", optimal_arima.order)

# Compare the optimal parameters with your chosen parameters (p=1, d=2, q=1)
your_parameters = (1, 2, 1)

if optimal_arima.order == your_parameters:
    print("Your chosen parameters are correct.")
else:
    print("Your chosen parameters are not optimal. The optimal parameters are:", optimal_arima.order)
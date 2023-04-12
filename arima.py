import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Read the CSV file
bitcoin_data = pd.read_csv('bitcoin_prices2.csv')

# Convert the 'Date' column to datetime objects
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])

# Remove commas from the 'Price' column and convert to float
bitcoin_data['Price'] = bitcoin_data['Price'].apply(lambda x: float(x.replace(',', '')))

# Set the 'Date' column as the DataFrame index
bitcoin_data.set_index('Date', inplace=True)

# Sort the DataFrame by index (date) and set the frequency to daily
bitcoin_data = bitcoin_data.asfreq('D').sort_index()

# Create the ARIMA model with p=1, d=2, and q=1
arima_model = ARIMA(bitcoin_data['Price'], order=(1, 2, 1))

# Fit the ARIMA model
model = arima_model.fit()

# Forecast the Bitcoin price for 1 day after the last record
forecast = model.forecast(steps=1)

# Calculate the date for 1 day after the last record
next_day = bitcoin_data.index[-1] + pd.Timedelta(days=1)

# Print the prediction
print(f"The prediction for {next_day.strftime('%Y-%m-%d')} is {forecast[0]:.2f}")
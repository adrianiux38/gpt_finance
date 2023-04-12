import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
data = pd.read_csv('bitcoinPrices.csv', delimiter='\t', skipinitialspace=True)

# Imprimir las columnas del DataFrame
print("Columnas en el DataFrame:", data.columns)

# Convertir la columna 'Date' en formato de fecha
data['Date'] = pd.to_datetime(data['Date'])

# Convertir los precios de string a float
data['Price'] = data['Price'].str.replace(',', '').astype(float)

# Establecer la columna 'Date' como índice
data.set_index('Date', inplace=True)

# Graficar el precio de Bitcoin
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Price'])
plt.xlabel('Fecha')
plt.ylabel('Precio de Bitcoin')
plt.title('Precio de Bitcoin a lo largo del tiempo')
plt.grid(True)
plt.show()
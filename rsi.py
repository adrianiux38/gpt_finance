import pandas as pd
import numpy as np

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    gains = deltas.copy()
    gains[gains < 0] = 0
    losses = -deltas.copy()
    losses[losses < 0] = 0

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    if avg_loss == 0:
        rsi = 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

    return rsi

# Leer el archivo CSV
data = pd.read_csv("bitcoin_prices.csv")

# Convertir la columna "Price" a números decimales
data["Price"] = data["Price"].str.replace(",", "").astype(float)

# Calcular el RSI de Bitcoin
rsi = calculate_rsi(data["Price"].values)

print(f"El RSI de Bitcoin es: {rsi:.2f}")
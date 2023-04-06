import requests

def get_crypto_fear_and_greed_index():
    url = "https://api.alternative.me/fng/?limit=1"
    response = requests.get(url)
    data = response.json()
    if "data" in data:
        return data["data"][0]["value_classification"], data["data"][0]["value"]
    else:
        return None, None

fear_and_greed_classification, fear_and_greed_value = get_crypto_fear_and_greed_index()

if fear_and_greed_classification and fear_and_greed_value:
    print(f"The current Crypto Fear and Greed Index is {fear_and_greed_value} ({fear_and_greed_classification}).")
else:
    print("Failed to fetch the Crypto Fear and Greed Index.")
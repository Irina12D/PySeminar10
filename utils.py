networks = ["BTC", "DASH", "LTC"]

# API URL
API_URL = "https://sochain.com/api/v2/"

# расчёт цены
def calc_price(data):
    prices = [float(element["price"]) for element in data["data"]["prices"]]
    return f"$ {(sum(prices) / len(prices)):.2f}"

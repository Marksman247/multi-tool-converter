import requests

API_KEY = "541335f3500f4529dc48dca9"

currencies = ["USD", "EUR", "NGN", "GBP", "JPY", "AUD"]

def convert_currency(amount, from_cur, to_cur):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_cur}"
    resp = requests.get(url)
    data = resp.json()

    if data.get("result") != "success":
        raise Exception(data.get("error-type", "Failed to fetch rates"))

    rates = data.get("conversion_rates", {})
    if to_cur not in rates:
        raise Exception(f"Unsupported currency: {to_cur}")

    converted = amount * rates[to_cur]
    return converted

import requests

API_KEY = 'fca_live_Uzui81zCVE45gjYPHwpfPeepZOz0uW5P1mku6nAY'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "GBP", "CAD", "EUR", "AUD", "CNY"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Unknown Currency")
        return None


while True:
    conv = input("Enter base currency (q to Quit) ").upper()
    if conv == 'Q' or conv == "":
        break
    data = convert_currency(conv)
    if data is not None:
        del data[conv]
        for ticker, value in data.items():
            print(f'{ticker}: {value}')
print("Bye...")
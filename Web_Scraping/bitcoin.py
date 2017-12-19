import requests

res = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')

data = res.json()

print("Buy at : Rs", data['buy'])
print("Sell at : Rs", data['sell'])

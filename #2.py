import requests

response = requests.get("https://books.toscrape.com/")
response_text = response.text

parts = response_text.split('price_color">')

for part in parts[1:]:
    price = part.split('<')[0]
    print(price)
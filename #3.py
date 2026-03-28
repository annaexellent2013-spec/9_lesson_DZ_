import requests

response = requests.get("https://books.toscrape.com/")
response_text = response.text

items = response_text.split('article class="product_pod"')[1:]

for item in items:
    title_part = item.split('title="')[1]
    title = title_part.split('"')[0]
    price_part = item.split('price_color">')[1]
    price = price_part.split('<')[0]
    avail_part = item.split('availability">')[1]
    availability = avail_part.split('</p>')[0]
    availability = " ".join(availability.split()).strip()
    print(title, price, availability)
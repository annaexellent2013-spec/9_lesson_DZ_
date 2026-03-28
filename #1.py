import requests

response = requests.get("https://books.toscrape.com/")
response_text = response.text

response_parse = response_text.split('class="product_pod"')

for parse_elem_1 in response_parse:
    if 'title="' in parse_elem_1:
        for parse_elem_2 in parse_elem_1.split('title="'):
            if parse_elem_2[0].isupper():
                title = parse_elem_2.split('"')[0]
                print(title)
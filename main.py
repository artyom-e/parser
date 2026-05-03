import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
URL = 'https://ooomalina.ru/catalog/zhenskij-trikotazh/platya-sarafany-zhenskie-trikotazhnye/'
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='item_info')

data = []

for prod in products:
    title = prod.find('div', class_='item-title')
    price = prod.find('span', class_='price_value')
    price_currency = prod.find('span', class_='price_currency')

    if title and price and price_currency:
        data.append(
            {'название': title.text.strip(), 'цена': price.text.strip() + ' ' + price_currency.text.strip(),})

df = pd.DataFrame(data)

df.to_excel('data.xlsx', index=False)

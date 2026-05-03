import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
URL = 'https://ooomalina.ru/catalog/zhenskij-trikotazh/platya-sarafany-zhenskie-trikotazhnye/'
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='price font-bold font_mxs')

products_title = soup.find_all('div', class_='item-title')
products_list = []
costs_list = []
for title in products_title:
    products_list.append(title.text.strip())

i = 0
for prodict in products:
    if i % 3 == 0: #due to cost is printed 3 times, we print the every third element
        costs_list.append(prodict.text.strip()[:-3])
    i += 1

df = pd.DataFrame({'название': products_list, 'цена': costs_list})
print(df)

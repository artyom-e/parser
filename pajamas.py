import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
base_url = 'https://ooomalina.ru/catalog/zhenskij-trikotazh/pizhamy-zhenskie-trikotazhnye/'

def get_data_pajamas():
    data = []
    for page in range(1, 12):
        URL = f'{base_url}?PAGEN_1={page}/'

        response = requests.get(URL, headers=headers)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code} на странице {page}")
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='item_info')

        for prod in products:
            title = prod.find('div', class_='item-title')
            price = prod.find('span', class_='price_value')
            price_currency = prod.find('span', class_='price_currency')
            ref = prod.find('a')['href']

            if title and price and price_currency:
                data.append(
                    {'название': title.text.strip(), 'цена': price.text.strip() + ' ' + price_currency.text.strip(),
                     'ссылка': ref})

    df = pd.DataFrame(data)
    df.to_excel('pajamas_data.xlsx', index=False)
    print('парсинг завершён')



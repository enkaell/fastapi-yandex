import datetime

from openpyxl import load_workbook
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import xml.etree.ElementTree as ET

path = 'yandex.xlsx'


def update_yandex_table():
    json_data = {"password": "RAMTRX1500", "regulation": True, "email": "Rakhmanov-2019@list.ru"}
    response = requests.post('https://www.sima-land.ru/api/v5/signin', json=json_data)
    token = response.json().get('token')
    tree = ET.parse('yandex.xml')
    root_node = tree.getroot()
    session = requests.Session()
    retry = Retry(connect=2, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    for tag in root_node.findall('shop/offers/offer'):
        try:
            response = session.get(
                f"https://www.sima-land.ru/api/v5/item/{tag.attrib['id']}",
                headers={
                    'accept': 'application/json',
                    'X-Api-Key': token,
                    'Authorization': token,
                },

                params={
                    'view': 'brief',
                    'by_sid': 'false',
                }
            )
        except Exception as e:
            tree.write('ostatki.xml', encoding='utf-8')
        tag.find('count').text = str(response.json()['balance'])
        print(response.json()['sid'], " обновлен")
    tree.write('ostatki.xml', encoding='utf-8')


update_yandex_table()

print("Ended in ", datetime.datetime.now())

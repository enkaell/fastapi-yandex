import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import zipfile
import datetime
from dataclasses import dataclass
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
path = 'yandex.xlsx'


# def update_yandex_table():
#     json_data = {"password": "RAMTRX1500", "regulation": True, "email": "Rakhmanov-2019@list.ru"}
#     response = requests.post('https://www.sima-land.ru/api/v5/signin', json=json_data)
#     token = response.json().get('token')
#     zip = zipfile.ZipFile('ostatki.zip')
#     zip.extractall()
#     dom = minidom.parse('t.xml')
#     elements = dom.getElelementByTagName
#     session = requests.Session()
#     retry = Retry(connect=2, backoff_factor=0.5)
#     adapter = HTTPAdapter(max_retries=retry)
#     session.mount('https://', adapter)
#     for tag in root_node.findall('shop/offers/offer'):
#         try:
#             tag.remove(tag[1])
#         except Exception:
#             pass
#         try:
#             response = session.get(
#                 f"https://www.sima-land.ru/api/v5/item/{tag.attrib['id']}",
#                 headers={
#                     'accept': 'application/json',
#                     'X-Api-Key': token,
#                     'Authorization': token,
#                 },
#
#                 params={
#                     'view': 'brief',
#                     'by_sid': 'false',
#                 }
#             )
#         except Exception as e:
#             tree.write('t.xml', encoding='utf-8')
#             zf = zipfile.ZipFile("ostatki.zip", "w", compresslevel=8, compression=zipfile.ZIP_DEFLATED)
#             zf.write('t.xml', compresslevel=8)
#         if int(tag.find('count').text) < 10:
#             tag.find('count').text = '0'
#         else:
#             tag.find('count').text = str(response.json()['balance'])
#     tree.write('t.xml', encoding='utf-8')
#     zf = zipfile.ZipFile("ostatki.zip", "w", compresslevel=8, compression=zipfile.ZIP_DEFLATED)
#     zf.write('t.xml', compresslevel=8)
#
# update_yandex_table()
# print("Ended in ", datetime.datetime.now())

dom = minidom.parse('t.xml')
elements = dom.getElelementsByTagName('shop/offers/offer')

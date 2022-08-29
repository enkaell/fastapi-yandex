from openpyxl import load_workbook
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import datetime

path = 'yandex.xlsx'
app = FastAPI()
Token = 123


@app.get("/", response_class=FileResponse)
async def main():
    return path


def update_yandex_table():
    json_data = {"password": "RAMTRX1500", "regulation": True, "email": "Rakhmanov-2019@list.ru"}
    response = requests.post('https://www.sima-land.ru/api/v5/signin', json=json_data)
    token = response.json().get('token')
    wb = load_workbook('yandex.xlsx')
    sheet = wb['Остатки']
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    start_time = int(time.time())
    for i in sheet['C'][3:]:
        response = session.get(
            f'https://www.sima-land.ru/api/v5/item/{i.value}',
            headers={
                'accept': 'application/json',
                'X-Api-Key': token,
                'Authorization': token,
            },

            params={
                'view': 'brief',
                'by_sid': 'false',
            },
            timeout=(6, 9)
        )
        sheet['E'][i.column].value = response.json()['balance']
        print(response.json()['sid'], " обновлен")

    wb.save('yandex.xlsx')
    return datetime.datetime.now()


date = update_yandex_table()
print(date)


@app.get("/time", response_class=FileResponse)
async def main():
    return date


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

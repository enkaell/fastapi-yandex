from openpyxl import load_workbook
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import datetime
from dataclasses import dataclass


@dataclass
class Date:
    date: str
    info: str


path = 'yandex.xml'
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
    Date.date = str(datetime.datetime.now())
    Date.info = "Ended"


@app.get("/start", response_class=FileResponse)
async def start():
    update_yandex_table()
    Date.date = str(datetime.datetime.now())
    Date.info = "Started"
    return f"Started at {datetime.datetime.now()}"


@app.get("/info")
async def get_info():
    return f"{Date.info} at {Date.date}"


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)

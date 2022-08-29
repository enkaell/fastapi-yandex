from typing import Union
import urllib.request
import requests
from fastapi import FastAPI, File, UploadFile, responses
from fastapi.responses import FileResponse

path = 'yappa.yaml'
app = FastAPI()
Token = 123


@app.get("/test/")
def read_root():
    return {"Hello": "World"}


@app.get("/", response_class=FileResponse)
async def main():
    return path

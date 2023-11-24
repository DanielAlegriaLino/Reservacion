import datetime

from fastapi import FastAPI
from modules import reservaciones
app = FastAPI()

@app.get('/RevisarMesas/{date}')
async def RevisarMesas(date: str = "2023-11-23" ):
    return reservaciones.RevisarMesas(date)
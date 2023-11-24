import datetime

from fastapi import FastAPI
from modules import reservaciones
app = FastAPI()

@app.get('/RevisarMesas/{date}')
async def RevisarMesas(date: str = "" ):
    return reservaciones.RevisarMesas(date)


import datetime

from fastapi import FastAPI
from modules import reservaciones
app = FastAPI()

@app.get('/RevisarMesas/{date}')
async def RevisarMesas(date: str = "" ):
    return reservaciones.RevisarMesas(date)

@app.delete("/BorrarReservacion/{hash}")
async def EliminarReservacion(hash: str):
    return reservaciones.BorrarReservacion(hash)


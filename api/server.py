import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules import reservaciones


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/RevisarMesas/{date}')
async def RevisarMesas(date: str = "" ):
    return reservaciones.RevisarMesas(date)

@app.delete("/BorrarReservacion/{hash}")
async def EliminarReservacion(hash: str):
    return reservaciones.BorrarReservacion(hash)

@app.get('/')
async def Root():
    return "UwU"
import datetime
import time
import asyncio

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

@app.get('/RevisarMesas/{date}', tags=['RevisarMesas'])
async def RevisarMesas(date: str = "" ):
    return reservaciones.RevisarMesas(date)

@app.delete("/BorrarReservacion/{hash}")
async def EliminarReservacion(hash: str):
    return reservaciones.BorrarReservacion(hash)

@app.post("/GenerarReservacion/{date}")
async def GenerarReservacion(date:str):
    id_created = reservaciones.GenerarReservacion(date)
    asyncio.create_task(EliminarReservacion(id_created))
    return id_created
    
async def EliminarReservacion(id_actual: int):
    await asyncio.sleep(30)
    reservaciones.BorrarReservacionTemporal(id_actual)
    
@app.get("/EstablecerReservacion/{date}/{id_temporal}/{mesa}")
async def EstablecerReservacion(date:str, id_temporal:int, mesa:int):
    print("Resedvacion")
    return reservaciones.EstablecerReservacion(date,mesa,id_temporal)

@app.get('/')
async def Root():
    return "UwU"
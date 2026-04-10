# -*- coding: utf-8 -*-

from fastapi import FastAPI
from routers import rt_server, rt_dbuser
from dotenv import load_dotenv

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduler import get_all_servers

# cargo las variables de entorno del fichero .env
load_dotenv()

app = FastAPI()

# registra los routers de servidores y usuarios
app.include_router(rt_server.router)
app.include_router(rt_dbuser.router)


# monitorizar estado de la API
@app.get("/health_check")
# async le dice a Python: "mientras esperas la respuesta de esto, atiende otras peticiones, no te quedes parado."
# async es no quedarse parado mientras esperas algo.
async def health_check():
    return {"status": "Ok"}


# crea el scheduler que ejecuta tareas en segundo plano
scheduler = AsyncIOScheduler()

# al arrancar la API, lanza el scheduler cada 30 segundos
@app.on_event("startup")
async def start():
    scheduler.add_job(get_all_servers, 'interval', seconds=30)
    scheduler.start()

# cuando apago o para la API, para el scheduler
@app.on_event("shutdown")
async def shutdown():
    scheduler.shutdown()
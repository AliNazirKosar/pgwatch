# -*- coding: utf-8 -*-

from pydantic import BaseModel
from enum import Enum

#In — lo que recibe la API del cliente. Lo que manda el usuario en el body del POST.
#Out — lo que devuelve la API al cliente. Lo que ve el usuario en la respuesta.

class MotorDB(str, Enum):
    postgresql = "postgresql"
    sqlserver = "sqlserver"
    mysql = "mysql"

class AddServerIn(BaseModel):
    server_name: str
    host: str
    port: int = 5432
    motor: MotorDB = MotorDB.postgresql

class AddServerOut(BaseModel):
    id : int
    server_name: str
    host: str
    port: int
    motor: MotorDB

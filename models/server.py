# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database import Base

class ServerDB(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    server_name = Column(String, nullable=False)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False, default=5432)
    motor = Column(String, nullable=False)
    status = Column(String, default="UNKNOWN")
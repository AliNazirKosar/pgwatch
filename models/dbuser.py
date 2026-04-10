# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class DbUser(Base):
    __tablename__ = "dbuser"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String, nullable=False)
    user_pass = Column(String, nullable=False)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False, unique=True)
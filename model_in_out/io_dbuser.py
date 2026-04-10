# -*- coding: utf-8 -*-

from pydantic import BaseModel


class DbuserIn(BaseModel):

    user: str
    user_pass: str
    server_id: int

class DbuserOut(BaseModel):

    id : int
    user: str
    server_id: int
# -*- coding: utf-8 -*-

from database import AsyncSessionLocal
from models.server import ServerDB
from models.dbuser import DbUser
from sqlalchemy import select
from utils.encrypt import decrypt_password
import asyncpg

async def get_all_servers():
    async with AsyncSessionLocal() as db:
        result =  await db.execute(select(ServerDB))
        servers_lst = result.scalars().all()

        for srv in servers_lst:
            result =  await db.execute(select(DbUser).filter(DbUser.server_id == srv.id))
            user = result.scalar_one_or_none()

            if not user:
                continue
            
            try:
                conn = await asyncpg.connect(
                    host = srv.host,
                    port = srv.port,
                    user = user.user,
                    password = decrypt_password(user.user_pass),
                    timeout= 10,
                    ssl="disable"
                )
                await conn.close()
                srv.status = "UP"
            except Exception:
                srv.status = "DOWN"

            await db.commit()

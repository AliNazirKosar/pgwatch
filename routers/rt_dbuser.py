# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException, Depends
from model_in_out.io_dbuser import DbuserIn, DbuserOut
from database import get_db
from models.dbuser import DbUser
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from utils.encrypt import encrypt_password

router = APIRouter(prefix="/dbuser")


@router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DbUser))
    allusers = result.scalars().all()
    if len(allusers) == 0:
        return {"mensaje": "No hay usuarios creados"}
    else:
        return allusers

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(DbUser).filter(DbUser.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/")
async def add_user(user: DbuserIn, db: AsyncSession = Depends(get_db)):
    
    new_user = DbUser(
        user = user.user,
        user_pass = encrypt_password(user.user_pass),
        server_id = user.server_id

    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

@router.put("/{user_id}")
async def modify_user(user_id: int, usuario: DbuserIn, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DbUser).filter(DbUser.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    user.user = usuario.user
    user.user_pass = encrypt_password(usuario.user_pass)
    await db.commit()
    await db.refresh(user)
    return user

@router.delete("/{user_id}")
async def delete_server(user_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(DbUser).filter(DbUser.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    await db.delete(user)
    await db.commit()

    return {"mensaje": "usuario eliminado"}
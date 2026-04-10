# -*- coding: utf-8 -*-


from fastapi import APIRouter, HTTPException, Depends
from model_in_out.io_server import AddServerIn, AddServerOut
from database import get_db
from models.server import ServerDB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

router = APIRouter(prefix="/server")

serverlst = []
counter = 1

@router.get("/")
async def get_all_servers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ServerDB))
    allserver = result.scalars().all()
    if len(allserver) == 0:
        return {"mensaje": "No hay servidores registrados"}
    else:
        return allserver
    """ if len(serverlst) == 0:
        return {"mensaje": "No hay servidores registrados"}
    return serverlst """

@router.get("/{server_id}")
async def get_server_by_id(server_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(ServerDB).filter(ServerDB.id == server_id))
    server = result.scalar_one_or_none()

    if not server:
        raise HTTPException(status_code=404, detail="Servidor no encontrado")
    return server
    
    """ for srv in serverlst:
        if server_id == srv.id:
            return srv
    raise HTTPException(status_code=404, detail="Servidor no encontrado") """

@router.post("/")
async def add_server(servidor: AddServerIn, db: AsyncSession = Depends(get_db)):
    
    new_server = ServerDB(**servidor.model_dump())
    db.add(new_server)
    await db.commit()
    await db.refresh(new_server)
    #global counter
    #new_server = AddServerOut(id=counter, **servidor.model_dump())
    #serverlst.append(new_server)
    #counter += 1
    
    return new_server

@router.put("/{server_id}")
async def modify_server(server_id: int, servidor: AddServerIn, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(ServerDB).filter(ServerDB.id == server_id))
    server = result.scalar_one_or_none()

    if not server:
        raise HTTPException(status_code=404, detail="Servidor no encontrado")
    else:
        server.server_name = servidor.server_name
        server.host = servidor.host
        server.port = servidor.port
        server.motor = servidor.motor
        await db.commit()
        await db.refresh(server)
        return {"mensaje": "servidor actualizado"}
    
    """ for i, srv in enumerate(serverlst):
        if server_id == srv.id:
            # se puede hacer de uno en uno como en este ejemplo
            # o podemos hacerlo de una con
            actualizado = AddServerOut(id=server_id, **servidor.model_dump())
            serverlst[i] = actualizado
            #srv.server_name = servidor.server_name
            #srv.host = servidor.host
            #srv.port = servidor.port
            #srv.motor = servidor.motor
            return actualizado """
    raise HTTPException(status_code=404, detail="Servidor no encontrado")

@router.delete("/{server_id}")
async def delete_server(server_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(ServerDB).filter(ServerDB.id == server_id))
    server = result.scalar_one_or_none()

    if not server:
        raise HTTPException(status_code=404, detail="Servidor no encontrado")
    else:
        await db.delete(server)
        await db.commit()
        return {"mensaje": "servidor eliminado"}
    #global serverlst
    #serverlst = [srv for srv in serverlst if srv.id != server_id]
    #return {"mensaje": "servidor eliminado"}


# En el codigo vemos que se declara global counter en la funcion post y delte
# esto es porque en python cuando suna variable está fuera de una función puedes
# leerla sin problema. Pero si quieres modificarla dentro de una función necesitas declarar global
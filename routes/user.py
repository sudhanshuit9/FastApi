
from config.db import conn
from models.index import users
from schemas.index import User



@user.get("/")
async def read_data():
    return conn.excute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return conn.excute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    conn.excute(users.select().values(
        name=user.name,
        email=user.email,
        password=user.password,
    ))
    return conn.excute(user.select()).fetchall()
@user.put("/{id}")
async def update_data(id:int,user: User):
    conn.excute(user.update(
        name=user.name,
        email=user.email,
        password=user.password,
    ).where(users.c.id == id))
    return conn.excute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    conn.excute(users.delete().where(users.c.id == id))
    return conn.excute(users.select()).fetchall()
from sqlalchemy import MetaData
from config.d import meta
from config.db import meta
users = Table(
    'users',meta,
    Column('id',Integers,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('password',String(255)),
)
from typing import Union,List
from routes.index import user
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.encoders import jsonable_encoder

app.include_router(user)


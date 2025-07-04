# app/main.py
from fastapi import FastAPI
from api.v1 import endpoints

app = FastAPI()
app.include_router(endpoints.router, prefix="/api/v1/users", tags=["Users"])

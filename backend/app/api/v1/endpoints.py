# app/api/v1/endpoints.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return [{"username": "user1"}, {"username": "user2"}]

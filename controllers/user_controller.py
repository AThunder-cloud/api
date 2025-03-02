# app/controllers/user_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.user_service import user_service
from app.schemas.user_schemas import UserCreate, UserResponse

class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/users", self.add_user, methods=["POST"], response_model=UserResponse)
        self.router.add_api_route("/users", self.list_users, methods=["GET"], response_model=list[UserResponse])
        self.router.add_api_route("/users/{id}", self.delete_user, methods=["DELETE"])
        self.router.add_api_route

    async def add_user(self, user: UserCreate, db: AsyncSession = Depends(get_db)):
        return await user_service.create_user(db, user)

    async def list_users(self, db: AsyncSession = Depends(get_db)):
        return await user_service.get_users(db)

    async def delete_user(self, id: int, db: AsyncSession = Depends(get_db)):
        return await user_service.delete_user(db, id)

# ✅ Create an instance of the controller
user_controller = UserController()

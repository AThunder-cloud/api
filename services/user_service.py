# app/services/user_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate,UserResponse

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, db: AsyncSession, user_data: UserCreate):
        return await self.user_repository.create_user(db, user_data)

    async def get_users(self, db: AsyncSession):
        return await self.user_repository.get_users(db)

    async def delete_user(self, db: AsyncSession, user_id: int):
        return await self.user_repository.delete_user(db, user_id)
    
    async def update_user(self,db:AsyncSession,user_data:UserResponse):
        return await self.user_repository.update_user(db,user_data)
# ✅ Create a Singleton Service Instance
user_service = UserService(UserRepository)

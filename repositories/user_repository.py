# app/repositories/user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user_schemas import UserCreate

class UserRepository:
    @staticmethod
    async def create_user(db: AsyncSession, user_data: UserCreate):
        user = User(name=user_data.name, email=user_data.email)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def get_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int):
        user = await db.get(User, user_id)
        if user:
            await db.delete(user)
            await db.commit()
            return {"message": "User deleted"}
        return {"error": "User not found"}

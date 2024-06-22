from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.models import AuthUser


async def get_auth_user(db: AsyncSession, user_id: int):
    async with db() as session:
        result = await session.execute(select(AuthUser).filter(AuthUser.id == user_id))
        return result.scalars().first()


async def get_auth_user_by_username(db: AsyncSession, username: str):
    async with db() as session:
        result = await session.execute(select(AuthUser).filter(AuthUser.username == username))
        return result.scalars().first()


async def create_auth_user(db: AsyncSession, user: AuthUser):
    async with db() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

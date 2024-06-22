from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_async_session


async def get_db() -> AsyncSession:
    async with get_async_session() as session:
        yield session

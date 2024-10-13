from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class BaseService:
    model = None

    @classmethod
    async def find_all(cls, session: AsyncSession, **filter_by):
        """Извлекает все записи, соответствующие фильтру."""
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

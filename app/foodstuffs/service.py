from typing import List, Optional
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.foodstuffs.exceptions import (
    FoodstuffMissingException,
    FoodstuffAlreadyExistException,
    FoodstuffAbsentException,
)
from app.foodstuffs.models import FoodStuff
from app.services.base import BaseService


class FoodstuffsService(BaseService):
    model = FoodStuff

    @classmethod
    async def existing_foodstuff_id(cls, session: AsyncSession, foodstuff_id: int):
        """Проверка существования продукта по id"""
        existing_foodstuff_id = await session.execute(select(cls.model).where(cls.model.id == foodstuff_id))
        return existing_foodstuff_id.scalar()

    @classmethod
    async def existing_foodstuff_name(cls, session: AsyncSession, foodstuff_name: str):
        """Проверка существования продукта по имени"""
        existing_foodstuff_name = await session.execute(select(cls.model).where(cls.model.name == foodstuff_name))
        return existing_foodstuff_name.scalar()

    @classmethod
    async def add_foodstuff(cls, session: AsyncSession, foodstuff_name: str):
        """Добавление нового продукта с указанным значениями."""
        # Проверяем на наличие названия
        if await cls.existing_foodstuff_name(session, foodstuff_name):
            # Здесь нужен логер
            raise FoodstuffAlreadyExistException(foodstuff_name)
        return await super().add(session, name=foodstuff_name)

    @classmethod
    async def find_one_or_none_foodstuff(cls, session: AsyncSession, foodstuff_id: int):
        """Поиск тега по идентификатору или создание исключения, если он не найден."""
        if not await cls.existing_foodstuff_id(session, foodstuff_id):
            # Здесь нужен логер
            raise FoodstuffAbsentException(foodstuff_id)
        return await super().find_one_or_none(session, id=foodstuff_id)

    @classmethod
    async def update_foodstuff(cls, session: AsyncSession, foodstuff_id: int, foodstuff_name: str):
        """Обновление существующего тега, если тег существует, а новое название не занято."""
        if not await cls.existing_foodstuff_id(session, foodstuff_id):
            raise FoodstuffAbsentException(foodstuff_id)
        if await cls.existing_foodstuff_name(session, foodstuff_name):
            raise FoodstuffAlreadyExistException(foodstuff_name)
        return await super().update(session, id=foodstuff_id, name=foodstuff_name)

    @classmethod
    async def delete_foodstuff(cls, session: AsyncSession, foodstuff_id: int):
        """Удаление тега по идентификатору, если он существует."""
        if not await cls.existing_foodstuff_id(session, foodstuff_id):
            raise FoodstuffAbsentException(foodstuff_id)
        return await super().delete(session, id=foodstuff_id)

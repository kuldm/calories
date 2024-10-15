from fastapi import APIRouter, Depends

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.foodstuffs.exceptions import OkStatusCode
from app.foodstuffs.schemas import FoodstuffsSchema
from app.foodstuffs.service import FoodstuffsService

router = APIRouter(
    prefix="/foodstuffs",
    tags=["Продукты питания"],
)


@router.get("",
            response_model=List[FoodstuffsSchema],
            description="Этот метод возвращает все продукты",
            )
async def get_foodstuffs(
        sessions: AsyncSession = Depends(get_db)
):
    return await FoodstuffsService.find_all(sessions)


@router.post("",
             response_model=FoodstuffsSchema,
             description="Этот метод создаёт продукт",
             )
async def create_foodstuff(
        foodstuff_name: str,
        sessions: AsyncSession = Depends(get_db),
):
    return await FoodstuffsService.add_foodstuff(sessions, foodstuff_name=foodstuff_name)


@router.get("/{foodstuff_id}",
            response_model=FoodstuffsSchema,
            description="Этот метод возвращает продукт по его ID",
            )
async def get_foodstuff(
        foodstuff_id: int,
        sessions: AsyncSession = Depends(get_db),
):
    return await FoodstuffsService.find_one_or_none_foodstuff(sessions, foodstuff_id=foodstuff_id)


@router.put("/{foodstuff_id}",
            response_model=FoodstuffsSchema,
            description="Этот метод обновляет данные продукта по его ID",
            )
async def update_tag(
        foodstuff_id: int,
        foodstuff_name: str,
        session: AsyncSession = Depends(get_db),
):
    return await FoodstuffsService.update_foodstuff(session, foodstuff_id=foodstuff_id, foodstuff_name=foodstuff_name)


@router.delete("/{foodstuff_id}",
               description="Этот метод удаляет продукт по его ID",
               )
async def delete_tag(
        foodstuff_id: int,
        session: AsyncSession = Depends(get_db),
):
    await FoodstuffsService.delete_foodstuff(session, foodstuff_id=foodstuff_id)
    return OkStatusCode().detail
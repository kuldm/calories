from fastapi import APIRouter, Depends

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.foodstuffs.schemas import FoodstuffsSchema
from app.foodstuffs.service import FoodstuffsService

router = APIRouter(
    prefix="/foodstuffs",
    tags=["Продукты питания"],
)


@router.get("",
            response_model=List[FoodstuffsSchema],
            description="Этот метод возвращает все продукты питания",
            )
async def get_foodstuffs(
        sessions: AsyncSession = Depends(get_db)
):
    return await FoodstuffsService.find_all(sessions)

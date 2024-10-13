from fastapi import APIRouter

router = APIRouter(
    prefix="/foodstuffs",
    tags=["Продукты питания"],
)

@router.get("")
async def get_foodstuffs():
    return "Редька"


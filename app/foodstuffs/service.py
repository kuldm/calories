from app.foodstuffs.models import FoodStuffs
from app.services.base import BaseService


class FoodstuffsService(BaseService):
    model = FoodStuffs
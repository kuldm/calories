from pydantic import BaseModel


class FoodstuffsSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
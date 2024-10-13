import uvicorn
from fastapi import FastAPI

from app.foodstuffs.router import router as foodstuffs_router

from app.config import settings

app = FastAPI(
    title="Calories App",
    version="0.1.0",
    root_path="/api",
)

app.include_router(foodstuffs_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT)

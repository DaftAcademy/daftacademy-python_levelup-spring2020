from fastapi import FastAPI
from .views import router as chinook_api_router

app = FastAPI()

app.include_router(chinook_api_router, tags=["chinook"])
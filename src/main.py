# src/main.py

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes import customers_route as customers
# from src.db import engine, metadata, database

# metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=[ "GET", "POST"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

app.include_router( customers.router, prefix="/customers", tags=["customers"])  # Alteração no include_router

import os
from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData, DateTime, func)
from dotenv import load_dotenv
from databases import Database

load_dotenv()
# Database url if none is passed the default one is used
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:88795842@localhost:5432/postgres")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("cpf", String(11), nullable=False, index=True                                                ),
    Column("birthdate", DateTime, nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, default=func.now())
)
# Databases query builder

database = Database(DATABASE_URL)

from datetime import datetime as dt
from pydantic import BaseModel, Field


class CustomerSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    cpf: str = Field(..., max_length=11)
    birthdate: dt


class CustomerDB(CustomerSchema):
    id: int
    created_at: dt

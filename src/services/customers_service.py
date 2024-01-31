from fastapi import HTTPException
from src.models.customers_model import CustomerSchema
from src.db import customers, database
from src.utils.cpf_validator import validate_cpf


async def create(payload: CustomerSchema):
    cleaned_cpf = validate_cpf(payload.cpf)

    cpf_exists_query = customers.select().where(cleaned_cpf == customers.c.cpf)
    existing_customer = await database.fetch_one(query=cpf_exists_query)
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer with this CPF already exists.")

    query = customers.insert().values(
        name=payload.name,
        cpf=cleaned_cpf,
        birthdate=payload.birthdate
    )
    await database.execute(query=query)
    return None

async def list_by_cpf(cpf: str):
    cleaned_cpf = ''.join(filter(str.isdigit, cpf))

    query = customers.select().where(cleaned_cpf == customers.c.cpf)
    customer = await database.fetch_one(query=query)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

async def list_all(page: int, size: int):
    query = customers.select().limit(size).offset((page - 1) * size)
    return await database.fetch_all(query=query)

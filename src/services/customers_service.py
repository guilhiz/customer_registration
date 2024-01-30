from src.models.customers_model import CustomerSchema
from src.db import customers, database


async def create(payload: CustomerSchema):
    # Implemente a validação do CPF aqui antes de inserir no banco
    # ...

    query = customers.insert().values(
        name=payload.name,
        cpf=payload.cpf,
        birthdate=payload.birthdate
    )
    return await database.execute(query=query)

async def list_by_cpf(cpf: str):
    query = customers.select().where(cpf == customers.c.cpf)
    return await database.fetch_one(query=query)

async def list_all(page: int, size: int):
    query = customers.select().limit(size).offset((page - 1) * size)
    return await database.fetch_all(query=query)

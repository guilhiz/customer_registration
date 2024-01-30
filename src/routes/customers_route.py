from typing import List
from fastapi import APIRouter, HTTPException, Query
from src.services import customers_service
from src.models.customers_model import CustomerDB, CustomerSchema
router = APIRouter()

@router.post("/", response_model=CustomerDB, status_code=201)
async def create(payload: CustomerSchema):
    existing_customer = await list_by_cpf(payload.cpf)
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer with this CPF already exists")
    customer = await customers_service.create(payload)
    return customer

@router.get("/{cpf}/", response_model=CustomerDB)
async def list_by_cpf(cpf: str):
    customer = await customers_service.list_by_cpf(cpf)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=List[CustomerDB])
async def list_all(page: int = Query(1, gt=0), size: int = Query(10, gt=0)):
    return await customers_service.list_all(page, size)

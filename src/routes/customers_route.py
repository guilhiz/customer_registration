from typing import List
import logging
from fastapi import APIRouter, Query
from src.services import customers_service
from src.models.customers_model import CustomerDB, CustomerSchema
router = APIRouter()
logging_level = "INFO"

logging.basicConfig(
    level=logging_level,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
)
logger = logging.getLogger("igma-api")

@router.post("/", response_model=str, status_code=201)
async def create(payload: CustomerSchema):
    try:
        await customers_service.create(payload)
        logger.info("Create Customer: Customer=%s", payload)
        return "Customer created successfully"
    except Exception as e:
        logger.error("Error in Create Customer: Error=%s", str(e))
        raise

@router.get("/{cpf}/", response_model=CustomerDB)
async def list_by_cpf(cpf: str):
    try:
        customer = await customers_service.list_by_cpf(cpf)
        logger.info("List Customer by CPF: CPF=%s", cpf)
        return customer
    except Exception as e:
        logger.error("Error in List Customer by CPF: CPF=%s Error=%s", cpf, str(e))
        raise

@router.get("/", response_model=List[CustomerDB])
async def list_all(page: int = Query(1, gt=0), size: int = Query(10, gt=0)):
    result = await customers_service.list_all(page, size)
    logger.info(
        "List All Customers: Page=%s Size=%s ResultCount=%s",
        page,
        size,
        len(result),
    )
    return result

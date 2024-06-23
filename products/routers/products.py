from fastapi import APIRouter, Depends
from typing import Annotated, List

from dependencies import get_product_service
from models import Product
from services import ProductService

router = APIRouter()


@router.get(
    "/product_lines/",
    tags=["products"],
    response_model=List[Product]
)
async def read_product_lines(service: Annotated[ProductService, Depends(get_product_service)]) -> List[Product]:
    product_lines = service.get_product_lines()
    return product_lines

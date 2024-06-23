from functools import lru_cache
from typing import Annotated
from fastapi import Depends

from config import Settings
from services import ProductService


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_product_service(settings: Annotated[Settings, Depends(get_settings)]) -> ProductService:
    service = ProductService(settings)
    return service

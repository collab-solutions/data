from functools import lru_cache
from typing import Annotated
from fastapi import Depends, FastAPI
from . import config

app = FastAPI()

@lru_cache
def get_settings() -> config.Settings:
    return config.Settings()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
  
@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {
      "account_uri": settings.account_uri,
      "account_key": settings.account_key,
    }

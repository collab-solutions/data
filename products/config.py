from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  account_uri: Optional[str] = None
  account_key: Optional[str] = None
  use_aad_auth: Optional[bool] = False
  aad_tenant_id: Optional[str] = None
  aad_client_id: Optional[str] = None
  aad_client_secret: Optional[str] = None

  model_config = SettingsConfigDict(env_file=".env")
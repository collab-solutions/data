from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  account_uri: str = ""
  account_key: str = ""
  use_aad_auth: bool = False
  create_if_not_exists: bool = False
  tenant_id: str = ""
  client_id: str = ""
  client_secret: str = ""
  database_name: str = ""

  model_config = SettingsConfigDict(env_file=".env")
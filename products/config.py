from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    account_uri: str = ""
    account_key: str = ""
    use_aad_auth: bool = False
    create_if_not_exists: bool = False
    tenant_id: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    database_name: str = ""
    max_item_count: int | None = None

    model_config = SettingsConfigDict(env_file=".env")

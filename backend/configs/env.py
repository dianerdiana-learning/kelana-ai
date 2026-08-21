from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    app_name: str = "Kelana AI"
    app_env: str = "development"
    app_debug: bool = True

    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


env = Env()

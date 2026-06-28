from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "TOKEN_AI"
    VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    MODEL_NAME: str = "chopratejas/kompress-v2-base"
    TOKENIZER_NAME: str = "answerdotai/ModernBERT-base"

    DEVICE: str = "auto"

    # Authentication
    DATABASE_URL: str = "sqlite:///./token_ai.db"
    API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
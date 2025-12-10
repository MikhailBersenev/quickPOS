"""
Конфигурация приложения
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Настройки приложения"""
    
    # JWT настройки
    SECRET_KEY: str = "your-secret-key-change-in-production"  # Должен быть в .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Время жизни токена в минутах
    
    # Настройки БД (можно использовать из dbconfig, но лучше через env)
    DATABASE_URL: Optional[str] = None
    
    # CORS настройки
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8080"]
    
    # Режим отладки
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


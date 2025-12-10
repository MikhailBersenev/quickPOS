"""
Главный файл приложения quickPOS
FastAPI сервер для системы управления продажами
"""
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import uvicorn
import logging

from app.core.config import settings
from app.api.v1.router import api_router

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Создание FastAPI приложения
app = FastAPI(
    title="quickPOS API",
    description="Fast and lightweight Point of Sale (POS) system API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Обработка исключений
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Обработка ошибок валидации запросов"""
    logger.warning(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Ошибка валидации данных",
            "errors": exc.errors()
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """Обработка ошибок базы данных"""
    logger.error(f"Database error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Ошибка при работе с базой данных",
            "error": str(exc)
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Обработка общих исключений"""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Внутренняя ошибка сервера",
            "error": str(exc) if settings.DEBUG else "Произошла непредвиденная ошибка"
        }
    )


# Подключение роутеров
app.include_router(api_router, prefix="/api/v1")


# Корневой эндпоинт
@app.get("/")
async def root():
    """Корневой эндпоинт API"""
    return {
        "message": "Добро пожаловать в quickPOS API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "redoc": "/api/redoc"
    }


# Health check эндпоинт
@app.get("/health")
async def health_check():
    """Проверка здоровья сервера"""
    return {
        "status": "healthy",
        "service": "quickPOS API"
    }


def main():
    """
    Точка входа для запуска сервера
    """
    import sys
    import os
    from pathlib import Path
    
    # Добавляем путь к backend в PYTHONPATH, если его там нет
    backend_dir = Path(__file__).parent.parent
    if str(backend_dir) not in sys.path:
        sys.path.insert(0, str(backend_dir))
    
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8000,
        reload=True,  # Автоперезагрузка при изменении кода (только для разработки)
        log_level="info",
        reload_dirs=[str(backend_dir)]  # Указываем директорию для отслеживания изменений
    )


if __name__ == "__main__":
    main()

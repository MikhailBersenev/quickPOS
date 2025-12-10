from pydantic import BaseModel, Field
from typing import Optional


class PositionBase(BaseModel):
    """Базовая схема должности"""
    name: str = Field(..., description="Название должности")
    level: int = Field(..., ge=0, description="Уровень должности")


class PositionCreate(PositionBase):
    """Схема для создания должности"""
    pass


class PositionUpdate(BaseModel):
    """Схема для обновления должности"""
    name: Optional[str] = Field(None, description="Название должности")
    level: Optional[int] = Field(None, ge=0, description="Уровень должности")
    isBlocked: Optional[bool] = Field(None, description="Заблокирована ли должность")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли должность")


class PositionResponse(PositionBase):
    """Схема для ответа с данными должности"""
    id: int
    isBlocked: Optional[bool] = None
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


from pydantic import BaseModel, Field
from typing import Optional


class DiscountBase(BaseModel):
    """Базовая схема скидки"""
    name: str = Field(..., description="Название скидки")
    description: Optional[str] = Field(None, description="Описание скидки")
    percent: Optional[float] = Field(None, ge=0, le=100, description="Процент скидки")
    sum: float = Field(..., ge=0, description="Сумма скидки")


class DiscountCreate(DiscountBase):
    """Схема для создания скидки"""
    pass


class DiscountUpdate(BaseModel):
    """Схема для обновления скидки"""
    name: Optional[str] = Field(None, description="Название скидки")
    description: Optional[str] = Field(None, description="Описание скидки")
    percent: Optional[float] = Field(None, ge=0, le=100, description="Процент скидки")
    sum: Optional[float] = Field(None, ge=0, description="Сумма скидки")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли скидка")


class DiscountResponse(DiscountBase):
    """Схема для ответа с данными скидки"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


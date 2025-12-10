from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class GoodCatBase(BaseModel):
    """Базовая схема категории товара"""
    name: str = Field(..., description="Название категории")
    description: str = Field(..., description="Описание категории")


class GoodCatCreate(GoodCatBase):
    """Схема для создания категории товара"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")


class GoodCatUpdate(BaseModel):
    """Схема для обновления категории товара"""
    name: Optional[str] = Field(None, description="Название категории")
    description: Optional[str] = Field(None, description="Описание категории")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли категория")


class GoodCatResponse(GoodCatBase):
    """Схема для ответа с данными категории товара"""
    id: int
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


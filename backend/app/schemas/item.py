from pydantic import BaseModel, Field
from typing import Optional


class ItemBase(BaseModel):
    """Базовая схема позиции (товар или услуга)"""
    batchId: Optional[int] = Field(None, description="ID партии (для товара)")
    serviceId: Optional[int] = Field(None, description="ID услуги")


class ItemCreate(ItemBase):
    """Схема для создания позиции"""
    pass


class ItemUpdate(BaseModel):
    """Схема для обновления позиции"""
    batchId: Optional[int] = Field(None, description="ID партии")
    serviceId: Optional[int] = Field(None, description="ID услуги")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли позиция")


class ItemResponse(ItemBase):
    """Схема для ответа с данными позиции"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


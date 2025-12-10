from pydantic import BaseModel, Field
from typing import Optional


class SaleBase(BaseModel):
    """Базовая схема продажи"""
    itemId: int = Field(..., description="ID позиции")
    qnt: int = Field(..., gt=0, description="Количество")
    VATRateId: int = Field(..., description="ID ставки НДС")
    sum: float = Field(..., gt=0, description="Сумма")
    comment: Optional[str] = Field(None, description="Комментарий")
    CheckId: int = Field(..., description="ID чека")


class SaleCreate(SaleBase):
    """Схема для создания продажи"""
    pass


class SaleUpdate(BaseModel):
    """Схема для обновления продажи"""
    itemId: Optional[int] = Field(None, description="ID позиции")
    qnt: Optional[int] = Field(None, gt=0, description="Количество")
    VATRateId: Optional[int] = Field(None, description="ID ставки НДС")
    sum: Optional[float] = Field(None, gt=0, description="Сумма")
    comment: Optional[str] = Field(None, description="Комментарий")
    CheckId: Optional[int] = Field(None, description="ID чека")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли продажа")


class SaleResponse(SaleBase):
    """Схема для ответа с данными продажи"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


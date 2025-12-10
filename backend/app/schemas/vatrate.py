from pydantic import BaseModel, Field
from typing import Optional


class VATRateBase(BaseModel):
    """Базовая схема ставки НДС"""
    name: str = Field(..., description="Название ставки НДС")
    rate: float = Field(..., ge=0, le=100, description="Ставка НДС в процентах")


class VATRateCreate(VATRateBase):
    """Схема для создания ставки НДС"""
    pass


class VATRateUpdate(BaseModel):
    """Схема для обновления ставки НДС"""
    name: Optional[str] = Field(None, description="Название ставки НДС")
    rate: Optional[float] = Field(None, ge=0, le=100, description="Ставка НДС в процентах")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли ставка НДС")


class VATRateResponse(VATRateBase):
    """Схема для ответа с данными ставки НДС"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


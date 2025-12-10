from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class BarcodeBase(BaseModel):
    """Базовая схема штрих-кода"""
    barcode: str = Field(..., description="Штрих-код")
    batchId: int = Field(..., description="ID партии")


class BarcodeCreate(BarcodeBase):
    """Схема для создания штрих-кода"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")


class BarcodeUpdate(BaseModel):
    """Схема для обновления штрих-кода"""
    barcode: Optional[str] = Field(None, description="Штрих-код")
    batchId: Optional[int] = Field(None, description="ID партии")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    isDeleted: Optional[bool] = Field(None, description="Удален ли штрих-код")


class BarcodeResponse(BarcodeBase):
    """Схема для ответа с данными штрих-кода"""
    id: int
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


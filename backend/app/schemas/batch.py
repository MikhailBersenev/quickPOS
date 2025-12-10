from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class BatchBase(BaseModel):
    """Базовая схема партии"""
    goodId: int = Field(..., description="ID товара")
    price: float = Field(..., gt=0, description="Цена")
    qnt: int = Field(..., gt=0, description="Количество")
    batchNumber: Optional[str] = Field(None, description="Номер партии")
    prodDate: date = Field(..., description="Дата производства")
    expDate: date = Field(..., description="Дата истечения срока годности")
    employeeId: int = Field(..., description="ID сотрудника")


class BatchCreate(BatchBase):
    """Схема для создания партии"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")
    writtenOff: bool = Field(False, description="Списана ли партия")


class BatchUpdate(BaseModel):
    """Схема для обновления партии"""
    goodId: Optional[int] = Field(None, description="ID товара")
    price: Optional[float] = Field(None, gt=0, description="Цена")
    qnt: Optional[int] = Field(None, gt=0, description="Количество")
    batchNumber: Optional[str] = Field(None, description="Номер партии")
    prodDate: Optional[date] = Field(None, description="Дата производства")
    expDate: Optional[date] = Field(None, description="Дата истечения срока годности")
    employeeId: Optional[int] = Field(None, description="ID сотрудника")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    writtenOff: Optional[bool] = Field(None, description="Списана ли партия")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли партия")


class BatchResponse(BatchBase):
    """Схема для ответа с данными партии"""
    id: int
    writtenOff: Optional[bool] = None
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


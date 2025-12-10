from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ServiceBase(BaseModel):
    """Базовая схема услуги"""
    name: str = Field(..., description="Название услуги")
    description: Optional[str] = Field(None, description="Описание услуги")
    price: float = Field(..., gt=0, description="Цена услуги")
    comment: Optional[str] = Field(None, description="Комментарий")
    CheckId: int = Field(..., description="ID чека")


class ServiceCreate(ServiceBase):
    """Схема для создания услуги"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")


class ServiceUpdate(BaseModel):
    """Схема для обновления услуги"""
    name: Optional[str] = Field(None, description="Название услуги")
    description: Optional[str] = Field(None, description="Описание услуги")
    price: Optional[float] = Field(None, gt=0, description="Цена услуги")
    comment: Optional[str] = Field(None, description="Комментарий")
    CheckId: Optional[int] = Field(None, description="ID чека")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли услуга")


class ServiceResponse(ServiceBase):
    """Схема для ответа с данными услуги"""
    id: int
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


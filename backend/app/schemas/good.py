from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class GoodBase(BaseModel):
    """Базовая схема товара"""
    name: str = Field(..., description="Название товара")
    description: str = Field(..., description="Описание товара")
    categoryId: int = Field(..., description="ID категории")
    imageUrl: Optional[str] = Field(None, description="URL изображения")
    isActive: bool = Field(True, description="Активен ли товар")
    discountId: int = Field(..., description="ID скидки")
    employeeId: int = Field(..., description="ID сотрудника")


class GoodCreate(GoodBase):
    """Схема для создания товара"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")


class GoodUpdate(BaseModel):
    """Схема для обновления товара"""
    name: Optional[str] = Field(None, description="Название товара")
    description: Optional[str] = Field(None, description="Описание товара")
    categoryId: Optional[int] = Field(None, description="ID категории")
    imageUrl: Optional[str] = Field(None, description="URL изображения")
    isActive: Optional[bool] = Field(None, description="Активен ли товар")
    discountId: Optional[int] = Field(None, description="ID скидки")
    employeeId: Optional[int] = Field(None, description="ID сотрудника")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    isDeleted: Optional[bool] = Field(None, description="Удален ли товар")


class GoodResponse(GoodBase):
    """Схема для ответа с данными товара"""
    id: int
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


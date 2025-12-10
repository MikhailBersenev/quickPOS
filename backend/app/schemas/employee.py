from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class EmployeeBase(BaseModel):
    """Базовая схема сотрудника"""
    lastName: str = Field(..., description="Фамилия")
    firstName: str = Field(..., description="Имя")
    middleName: Optional[str] = Field(None, description="Отчество")
    positionId: int = Field(..., description="ID должности")
    userId: int = Field(..., description="ID пользователя")


class EmployeeCreate(EmployeeBase):
    """Схема для создания сотрудника"""
    updateDate: date = Field(default_factory=date.today, description="Дата обновления")


class EmployeeUpdate(BaseModel):
    """Схема для обновления сотрудника"""
    lastName: Optional[str] = Field(None, description="Фамилия")
    firstName: Optional[str] = Field(None, description="Имя")
    middleName: Optional[str] = Field(None, description="Отчество")
    positionId: Optional[int] = Field(None, description="ID должности")
    userId: Optional[int] = Field(None, description="ID пользователя")
    updateDate: Optional[date] = Field(None, description="Дата обновления")
    isDeleted: Optional[bool] = Field(None, description="Удален ли сотрудник")


class EmployeeResponse(EmployeeBase):
    """Схема для ответа с данными сотрудника"""
    id: int
    updateDate: date
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


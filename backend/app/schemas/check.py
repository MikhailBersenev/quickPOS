from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, List, TYPE_CHECKING
from datetime import date as date_type, time as time_type
import datetime as dt

if TYPE_CHECKING:
    from .sale import SaleResponse


class CheckBase(BaseModel):
    """Базовая схема чека"""
    check_date: date_type = Field(
        default_factory=date_type.today,
        description="Дата чека",
        alias="date"
    )
    check_time: time_type = Field(
        default_factory=lambda: dt.datetime.now().time(),
        description="Время чека",
        alias="time"
    )
    totalAmount: float = Field(..., ge=0, description="Общая сумма")
    discountAmount: float = Field(0, ge=0, description="Сумма скидки")
    employeeId: int = Field(..., description="ID сотрудника")

    class Config:
        populate_by_name = True


class CheckCreate(CheckBase):
    """Схема для создания чека"""
    pass


class CheckUpdate(BaseModel):
    """Схема для обновления чека"""
    check_date: Optional[date_type] = Field(None, description="Дата чека", alias="date")
    check_time: Optional[time_type] = Field(None, description="Время чека", alias="time")
    totalAmount: Optional[float] = Field(None, ge=0, description="Общая сумма")
    discountAmount: Optional[float] = Field(None, ge=0, description="Сумма скидки")
    employeeId: Optional[int] = Field(None, description="ID сотрудника")
    isDeleted: Optional[bool] = Field(None, description="Удален ли чек")

    class Config:
        populate_by_name = True


class CheckResponse(CheckBase):
    """Схема для ответа с данными чека"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class CheckWithSales(CheckResponse):
    """Схема чека с продажами"""
    sales: List['SaleResponse'] = Field(default_factory=list, description="Список продаж")

    class Config:
        from_attributes = True
        populate_by_name = True


# Forward reference будет разрешен в __init__.py после импорта всех схем

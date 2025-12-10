from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class UserBase(BaseModel):
    """Базовая схема пользователя"""
    name: str = Field(..., description="Имя пользователя")
    roleId: int = Field(..., description="ID роли")


class UserCreate(UserBase):
    """Схема для создания пользователя"""
    password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")


class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    name: Optional[str] = Field(None, description="Имя пользователя")
    password: Optional[str] = Field(None, min_length=6, description="Пароль")
    roleId: Optional[int] = Field(None, description="ID роли")
    isDeleted: Optional[bool] = Field(None, description="Удален ли пользователь")


class UserResponse(UserBase):
    """Схема для ответа с данными пользователя"""
    id: int
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


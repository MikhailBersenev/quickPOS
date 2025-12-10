from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Token(BaseModel):
    """Схема токена доступа"""
    access_token: str = Field(..., description="JWT токен доступа")
    token_type: str = Field(default="bearer", description="Тип токена")


class TokenData(BaseModel):
    """Данные из токена"""
    username: Optional[str] = None
    user_id: Optional[int] = None


class LoginRequest(BaseModel):
    """Схема для входа в систему"""
    username: str = Field(..., description="Имя пользователя")
    password: str = Field(..., description="Пароль")


class LoginResponse(BaseModel):
    """Схема ответа при входе"""
    access_token: str = Field(..., description="JWT токен доступа")
    token_type: str = Field(default="bearer", description="Тип токена")
    user: 'UserResponse' = Field(..., description="Данные пользователя")


class PasswordChange(BaseModel):
    """Схема для смены пароля"""
    old_password: str = Field(..., description="Старый пароль")
    new_password: str = Field(..., min_length=6, description="Новый пароль (минимум 6 символов)")


# Разрешаем forward reference
from .user import UserResponse
LoginResponse.model_rebuild()


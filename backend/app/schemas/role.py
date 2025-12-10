from pydantic import BaseModel, Field
from typing import Optional


class RoleBase(BaseModel):
    """Базовая схема роли"""
    name: str = Field(..., description="Название роли")
    level: int = Field(..., ge=0, description="Уровень доступа")


class RoleCreate(RoleBase):
    """Схема для создания роли"""
    pass


class RoleUpdate(BaseModel):
    """Схема для обновления роли"""
    name: Optional[str] = Field(None, description="Название роли")
    level: Optional[int] = Field(None, ge=0, description="Уровень доступа")
    isBlocked: Optional[bool] = Field(None, description="Заблокирована ли роль")
    isDeleted: Optional[bool] = Field(None, description="Удалена ли роль")


class RoleResponse(RoleBase):
    """Схема для ответа с данными роли"""
    id: int
    isBlocked: Optional[bool] = None
    isDeleted: Optional[bool] = None

    class Config:
        from_attributes = True


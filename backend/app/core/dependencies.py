"""
Зависимости для FastAPI (dependency injection)
"""
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import SessionLocal
from app.models import Users, Roles
from app.core.security import decode_access_token, verify_password
from app.schemas.auth import TokenData

# OAuth2 схема для получения токена из заголовка Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


async def get_db() -> AsyncSession:
    """
    Dependency для получения сессии БД.
    Автоматически закрывает сессию после использования.
    """
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> Users:
    """
    Dependency для получения текущего пользователя из JWT токена.
    
    Raises:
        HTTPException: Если токен невалидный или пользователь не найден
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось подтвердить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Декодируем токен
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    
    # Извлекаем данные из токена
    user_id: Optional[int] = payload.get("sub")
    if user_id is None:
        raise credentials_exception
    
    token_data = TokenData(user_id=user_id, username=payload.get("username"))
    
    # Получаем пользователя из БД
    result = await db.execute(
        select(Users).where(
            Users.id == token_data.user_id,
            Users.isDeleted == False
        )
    )
    user = result.scalar_one_or_none()
    
    if user is None:
        raise credentials_exception
    
    return user


async def get_current_active_user(
    current_user: Users = Depends(get_current_user)
) -> Users:
    """
    Dependency для проверки, что пользователь активен (не удален).
    """
    if current_user.isDeleted:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Пользователь неактивен"
        )
    return current_user


async def get_current_user_role(
    current_user: Users = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
) -> Roles:
    """
    Dependency для получения роли текущего пользователя.
    """
    result = await db.execute(
        select(Roles).where(
            Roles.id == current_user.roleId,
            Roles.isDeleted == False,
            Roles.isBlocked == False
        )
    )
    role = result.scalar_one_or_none()
    
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Роль пользователя не найдена или заблокирована"
        )
    
    return role


def require_role(min_level: int):
    """
    Фабрика для создания dependency, проверяющей минимальный уровень доступа.
    
    Args:
        min_level: Минимальный уровень доступа (из таблицы roles.level)
        
    Returns:
        Dependency функция
    """
    async def check_role(
        current_role: Roles = Depends(get_current_user_role)
    ) -> Roles:
        if current_role.level < min_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Недостаточно прав. Требуется уровень доступа {min_level} или выше"
            )
        return current_role
    
    return check_role


# Предопределенные зависимости для разных уровней доступа
# Можно использовать: Depends(require_admin), Depends(require_manager) и т.д.

async def require_admin(current_role: Roles = Depends(require_role(100))):
    """Требует уровень доступа администратора (100+)"""
    return current_role


async def require_manager(current_role: Roles = Depends(require_role(50))):
    """Требует уровень доступа менеджера (50+)"""
    return current_role


async def require_cashier(current_role: Roles = Depends(require_role(10))):
    """Требует уровень доступа кассира (10+)"""
    return current_role


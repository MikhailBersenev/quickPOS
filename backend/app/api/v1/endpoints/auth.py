"""
Эндпоинты для аутентификации
"""
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.dependencies import get_db
from app.models import Users, Roles
from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.config import settings
from app.core.dependencies import get_current_active_user
from app.schemas.auth import LoginRequest, LoginResponse, Token, PasswordChange
from app.schemas.user import UserResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Вход в систему.
    
    Проверяет имя пользователя и пароль, возвращает JWT токен.
    """
    # Ищем пользователя по имени
    result = await db.execute(
        select(Users).where(
            Users.name == login_data.username,
            Users.isDeleted == False
        )
    )
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль"
        )
    
    # Проверяем пароль
    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль"
        )
    
    # Проверяем, что роль не заблокирована
    role_result = await db.execute(
        select(Roles).where(
            Roles.id == user.roleId,
            Roles.isDeleted == False,
            Roles.isBlocked == False
        )
    )
    role = role_result.scalar_one_or_none()
    
    if not role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Роль пользователя заблокирована или удалена"
        )
    
    # Создаем токен
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "username": user.name, "role_id": user.roleId},
        expires_delta=access_token_expires
    )
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            name=user.name,
            roleId=user.roleId,
            isDeleted=user.isDeleted
        )
    )


@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: Users = Depends(get_current_active_user)
):
    """
    Получить информацию о текущем пользователе.
    """
    return UserResponse(
        id=current_user.id,
        name=current_user.name,
        roleId=current_user.roleId,
        isDeleted=current_user.isDeleted
    )


@router.post("/change-password")
async def change_password(
    password_data: PasswordChange,
    current_user: Users = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Смена пароля текущего пользователя.
    """
    # Проверяем старый пароль
    if not verify_password(password_data.old_password, current_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неверный текущий пароль"
        )
    
    # Обновляем пароль
    current_user.password = get_password_hash(password_data.new_password)
    await db.commit()
    await db.refresh(current_user)
    
    return {"message": "Пароль успешно изменен"}


@router.post("/logout")
async def logout():
    """
    Выход из системы.
    
    Примечание: В JWT токенах выход реализуется на клиенте
    путем удаления токена. На сервере можно добавить blacklist токенов
    для более строгого контроля.
    """
    return {"message": "Успешный выход из системы"}


# Система авторизации quickPOS

## Обзор

Система авторизации использует **JWT (JSON Web Tokens)** для аутентификации и **ролевую модель доступа** на основе уровней (levels) для авторизации.

## Как это работает

### 1. Аутентификация (Authentication)

#### Процесс входа:

1. **Клиент отправляет запрос** на `/api/v1/auth/login` с именем пользователя и паролем:
   ```json
   {
     "username": "admin",
     "password": "password123"
   }
   ```

2. **Сервер проверяет**:
   - Существует ли пользователь с таким именем
   - Не удален ли пользователь (`isDeleted == False`)
   - Правильный ли пароль (сравнение с хешем в БД)
   - Активна ли роль пользователя (`Roles.isBlocked == False`)

3. **Сервер создает JWT токен** с данными:
   - `sub` (subject) - ID пользователя
   - `username` - имя пользователя
   - `role_id` - ID роли
   - `exp` - время истечения токена
   - `iat` - время создания токена

4. **Сервер возвращает токен**:
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "bearer",
     "user": {
       "id": 1,
       "name": "admin",
       "roleId": 1,
       "isDeleted": false
     }
   }
   ```

5. **Клиент сохраняет токен** (обычно в localStorage или cookies)

#### Использование токена:

Клиент отправляет токен в заголовке каждого запроса:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### 2. Авторизация (Authorization)

#### Ролевая модель:

Система использует **уровни доступа** из таблицы `roles`:

- **Уровень 100+** - Администратор (полный доступ)
- **Уровень 50-99** - Менеджер (управление товарами, продажами)
- **Уровень 10-49** - Кассир (только продажи)
- **Уровень 0-9** - Гость (только просмотр)

#### Проверка доступа:

1. **Dependency `get_current_user`**:
   - Извлекает токен из заголовка `Authorization`
   - Декодирует JWT токен
   - Получает пользователя из БД
   - Проверяет, что пользователь не удален

2. **Dependency `get_current_user_role`**:
   - Получает роль пользователя из БД
   - Проверяет, что роль не заблокирована и не удалена

3. **Dependency `require_role(min_level)`**:
   - Проверяет, что уровень доступа роли >= `min_level`
   - Вызывает исключение, если доступ запрещен

#### Примеры использования:

```python
# Требуется любой авторизованный пользователь
@router.get("/products")
async def get_products(current_user: Users = Depends(get_current_active_user)):
    ...

# Требуется кассир (уровень 10+)
@router.post("/sales/check")
async def create_check(
    current_role: Roles = Depends(require_cashier)
):
    ...

# Требуется менеджер (уровень 50+)
@router.post("/products")
async def create_product(
    current_role: Roles = Depends(require_manager)
):
    ...

# Требуется администратор (уровень 100+)
@router.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    current_role: Roles = Depends(require_admin)
):
    ...
```

### 3. Безопасность паролей

- Пароли **никогда не хранятся в открытом виде**
- Используется **bcrypt** для хеширования
- При создании пользователя пароль хешируется: `get_password_hash(password)`
- При проверке пароля: `verify_password(plain_password, hashed_password)`

### 4. Структура файлов

```
backend/app/
├── core/
│   ├── config.py          # Настройки (SECRET_KEY, время жизни токена)
│   ├── security.py        # Функции для работы с паролями и JWT
│   └── dependencies.py    # FastAPI dependencies для проверки доступа
├── api/v1/endpoints/
│   └── auth.py           # Эндпоинты: /login, /me, /logout, /change-password
└── schemas/
    └── auth.py           # Pydantic схемы для авторизации
```

## Эндпоинты

### POST `/api/v1/auth/login`
Вход в систему. Возвращает JWT токен.

**Запрос:**
```json
{
  "username": "admin",
  "password": "password123"
}
```

**Ответ:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "name": "admin",
    "roleId": 1,
    "isDeleted": false
  }
}
```

### GET `/api/v1/auth/me`
Получить информацию о текущем пользователе.

**Требуется:** Авторизация (токен в заголовке)

**Ответ:**
```json
{
  "id": 1,
  "name": "admin",
  "roleId": 1,
  "isDeleted": false
}
```

### POST `/api/v1/auth/change-password`
Смена пароля текущего пользователя.

**Требуется:** Авторизация

**Запрос:**
```json
{
  "old_password": "oldpass123",
  "new_password": "newpass456"
}
```

### POST `/api/v1/auth/logout`
Выход из системы (на клиенте удаляется токен).

## Настройка

### Переменные окружения (.env):

```env
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
```

**ВАЖНО:** В продакшене используйте сильный случайный SECRET_KEY!

## Безопасность

1. **Токены имеют срок действия** (по умолчанию 30 минут)
2. **Пароли хешируются** с помощью bcrypt
3. **Роли проверяются** на каждом запросе
4. **Soft delete** - удаленные пользователи не могут войти
5. **Заблокированные роли** - пользователи с заблокированными ролями не могут войти

## Расширение

### Blacklist токенов (опционально):

Для более строгого контроля можно добавить blacklist недействительных токенов:

```python
# В Redis или БД хранить список недействительных токенов
# При logout добавлять токен в blacklist
# При проверке токена проверять, не в blacklist ли он
```

### Refresh токены (опционально):

Для длительных сессий можно добавить refresh токены с большим сроком жизни.

## Пример использования на клиенте

```javascript
// Вход
const response = await fetch('/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: 'admin', password: 'pass123' })
});
const { access_token } = await response.json();
localStorage.setItem('token', access_token);

// Запрос с токеном
const data = await fetch('/api/v1/products', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('token')}`
  }
});
```


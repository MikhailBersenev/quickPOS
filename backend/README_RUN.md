# Инструкция по запуску quickPOS API

## Установка зависимостей

1. Создайте виртуальное окружение (рекомендуется):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

2. Установите зависимости:
```bash
pip install -r ../requirements.txt
```

## Настройка

1. Создайте файл `.env` в корне проекта (или в папке `backend/app`):
```env
SECRET_KEY=your-super-secret-key-change-in-production-min-32-characters
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256
DEBUG=True
```

2. Убедитесь, что база данных PostgreSQL доступна и настройки в `app/dbconfig.py` корректны.

## Запуск сервера

### Вариант 1: Через Python
```bash
cd backend/app
python main.py
```

### Вариант 2: Через uvicorn напрямую
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Вариант 3: Через uvicorn из корня проекта
```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

## Проверка работы

После запуска сервера:

1. Откройте в браузере документацию API:
   - Swagger UI: http://localhost:8000/api/docs
   - ReDoc: http://localhost:8000/api/redoc

2. Проверьте корневой эндпоинт:
   ```bash
   curl http://localhost:8000/
   ```

3. Проверьте health check:
   ```bash
   curl http://localhost:8000/health
   ```

## Эндпоинты

- `GET /` - Корневой эндпоинт
- `GET /health` - Проверка здоровья сервера
- `POST /api/v1/auth/login` - Вход в систему
- `GET /api/v1/auth/me` - Информация о текущем пользователе
- `POST /api/v1/auth/logout` - Выход из системы
- `POST /api/v1/auth/change-password` - Смена пароля

## Устранение проблем

### Ошибка импорта модулей
Если возникают ошибки импорта, убедитесь что вы запускаете из правильной директории или используйте:
```bash
PYTHONPATH=/path/to/quickPOS/backend python -m app.main
```

### Ошибка подключения к БД
Проверьте:
- Доступность PostgreSQL сервера
- Настройки в `app/dbconfig.py`
- Правильность строки подключения

### Порт занят
Если порт 8000 занят, измените его в `main.py` или используйте:
```bash
uvicorn app.main:app --reload --port 8001
```


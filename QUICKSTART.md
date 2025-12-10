# Быстрый старт quickPOS

## Шаг 1: Установка зависимостей

Убедитесь, что виртуальное окружение активировано, затем установите зависимости:

```bash
# Активируйте виртуальное окружение (если еще не активировано)
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows

# Установите зависимости
pip install -r requirements.txt
```

Если что-то не установилось, установите вручную:
```bash
pip install 'fastapi' 'uvicorn[standard]' 'pydantic' 'pydantic-settings' \
    'python-jose[cryptography]' 'passlib[bcrypt]' 'sqlalchemy' 'asyncpg'
```

## Шаг 2: Настройка (опционально)

Создайте файл `.env` в корне проекта:
```env
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
```

## Шаг 3: Запуск сервера

### Вариант 1: Используя скрипт запуска (рекомендуется)
```bash
cd backend
python run_server.py
```

### Вариант 2: Через uvicorn напрямую
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Вариант 3: Через функцию main()
```bash
cd backend
python -m app.main
```

## Шаг 4: Откройте документацию

После запуска откройте в браузере:
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

## Проверка работы

```bash
# Проверка корневого эндпоинта
curl http://localhost:8000/

# Проверка health check
curl http://localhost:8000/health
```

## Устранение проблем

### Ошибка "ModuleNotFoundError: No module named 'app'"
Убедитесь, что вы запускаете из директории `backend`:
```bash
cd backend
python run_server.py
```

### Ошибка импорта модулей
Убедитесь, что все зависимости установлены:
```bash
pip install -r requirements.txt
```

### Порт занят
Если порт 8000 занят, измените его в `run_server.py` или используйте:
```bash
uvicorn app.main:app --reload --port 8001
```

---

**Готово!** Сервер должен запуститься и быть доступен по адресу http://localhost:8000

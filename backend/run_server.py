#!/usr/bin/env python3
"""
Скрипт для запуска quickPOS сервера
Использование: python run_server.py
"""
import sys
import os
from pathlib import Path

# Добавляем путь к backend в PYTHONPATH
backend_dir = Path(__file__).parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 50)
    print("Запуск quickPOS API сервера...")
    print("=" * 50)
    print(f"Backend директория: {backend_dir}")
    print(f"Python path включает: {backend_dir in [Path(p) for p in sys.path]}")
    print("=" * 50)
    
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8000,
        reload=True,
        log_level="info",
        reload_dirs=[str(backend_dir)]
    )


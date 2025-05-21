#!/bin/bash

# Активация виртуального окружения
source venv/bin/activate

# Проверка зависимостей
pip install -r requirements.txt

# Запуск FastAPI сервера
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

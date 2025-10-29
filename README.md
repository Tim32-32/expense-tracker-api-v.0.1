# 💰 Expense Tracker API

Простое REST API для отслеживания расходов. Реализовано на FastAPI + SQLAlchemy + Alembic.

## 🚀 Возможности

- Добавление, редактирование и удаление расходов
- Валидация данных через Pydantic-схемы
- Хранение данных в MySQL
- Миграции через Alembic
- Swagger-документация на `/docs`

## 📦 Установка и запуск

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/your-username/expense_tracker_api.git
   cd expense_tracker_api
2. Активируй виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # или .venv\Scripts\activate на Windows
3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
4. Запусти приложение:
   uvicorn app.main:app --reload
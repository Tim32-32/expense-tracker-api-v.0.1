#  Expense Tracker API

<<<<<<< HEAD
Простое REST API для отслеживания расходов.

##  Технологии

Python 3.11+

FastAPI

SQLAlchemy

Alembic (миграции базы данных)

Pydantic

MySQL

Ruff (линтер)

Pytest 
=======
Простое REST API для отслеживания расходов. Реализовано на FastAPI + SQLAlchemy + Alembic.
>>>>>>> 4ad488c86271d4c19f1cb64b656e1ec823440cef

##  Возможности

- Добавление, редактирование и удаление расходов
- Валидация данных через Pydantic-схемы
- Хранение данных в MySQL
- Миграции через Alembic
- Swagger-документация на `/docs`

<<<<<<< HEAD
## Установка и запуск
=======
##  Установка и запуск
>>>>>>> 4ad488c86271d4c19f1cb64b656e1ec823440cef

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
<<<<<<< HEAD
   uvicorn app.main:app --reload
=======
   ```bash
   uvicorn app.main:app --reload
>>>>>>> 4ad488c86271d4c19f1cb64b656e1ec823440cef

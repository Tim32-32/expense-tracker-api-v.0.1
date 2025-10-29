from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.expense_model import Expense
from app.shemas.expense_shema import ExpenseCreate
from datetime import datetime

def create_expense_in_db(db: Session, expense_data: ExpenseCreate) -> Expense:
    expense_date = expense_data.date or datetime.utcnow()
    db_expense = Expense(
        amount=expense_data.amount,
        category=expense_data.category,
        description=expense_data.description,
        date=expense_date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense_by_id_or_404(db: Session, expense_id: int) -> Expense:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Расход не найден")
    return expense

def get_all_expenses(db: Session) -> list[Expense]:
    return db.query(Expense).order_by(Expense.date.desc()).all()

def delete_expense_by_id_or_404(db: Session, expense_id: int) -> Expense:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Расход не найден")
    db.delete(expense)
    db.commit()
    return expense

def add_expense(db: Session, expense_data: ExpenseCreate) -> Expense:
    existing_expense = db.query(Expense).filter(Expense.id == expense_data.id).first()
    if existing_expense:
        raise HTTPException(status_code=409, detail="Айди уже существует")

    new_expense = Expense(**expense_data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
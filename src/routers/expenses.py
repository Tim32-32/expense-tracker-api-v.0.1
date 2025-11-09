from fastapi import APIRouter, Depends
from src.schemas import ExpenseCreate
from src.crud import create_expense, get_expenses_by_user, perform_delete_expense
from src.db import get_db
from sqlalchemy.orm import Session
from src.auth import get_current_user

router = APIRouter()


@router.post("/")
def add_expense(exp: ExpenseCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return create_expense(db, exp.amount, exp.category, exp.description, current_user.id)

@router.get("/")
def list_expenses(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_expenses_by_user(db, current_user.id)

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return perform_delete_expense(db, expense_id, current_user)

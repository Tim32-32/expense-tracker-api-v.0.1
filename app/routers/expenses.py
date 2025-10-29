from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.expense_service import get_all_expenses, delete_expense_by_id_or_404, add_expense
from app.models.expense_model import Expense
from app.shemas.expense_shema import ExpenseCreate, ExpenseOut
from app.services.expense_service import create_expense_in_db, get_expense_by_id_or_404


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense_in_db(db, expense)

@router.get("/{expense_id}", response_model=ExpenseOut)
def get_expense_by_id(expense_id: int = Path(..., description="ID расхода"), db: Session = Depends(get_db)):
    return get_expense_by_id_or_404(db, expense_id)

@router.get("/", response_model=list[ExpenseOut])
def all_expenses(db: Session = Depends(get_db)):
    return get_all_expenses(db)

@router.delete("/{expense_id}", response_model=ExpenseOut)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return delete_expense_by_id_or_404(db, expense_id)

@router.post("/", response_model=ExpenseOut)
def add_expense_in_db(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return add_expense(db, expense)
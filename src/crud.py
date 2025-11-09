from passlib.context import CryptContext
from src.models import User, Expense
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, email: str, password: str) -> User:
    hashed_password = pwd_context.hash(password)
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_expense(db, amount, category, description, user_id, date=None):
    if date is None:
        expense = Expense(amount=amount, category=category, description=description, user_id=user_id)
    else:
        expense = Expense(amount=amount, category=category, description=description, user_id=user_id, date=date)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def get_expenses_by_user(db: Session, user_id: int) -> list[Expense]:
    return db.query(Expense).filter(Expense.user_id == user_id).all()


def perform_delete_expense(db: Session, expense_id: int, current_user):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
    db.delete(expense)
    db.commit()
    return {"status": "deleted", "id": expense_id}

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None


class ExpenseShow(BaseModel):
    id : int
    amount: float
    category: str
    description: Optional[str]
    date: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

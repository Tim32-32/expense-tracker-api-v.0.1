from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None
    date: Optional[datetime] = None

class ExpenseOut(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str]
    date: datetime

    class Config:
        orm_mode = True
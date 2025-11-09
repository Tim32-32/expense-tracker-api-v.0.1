from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()  # Тут — магия создания "родителя" для всех моделей

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # уникальный ключ — id
    email = Column(String(120), unique=True, index=True, nullable=False)
    hashed_password = Column(String(64), nullable=False)
    expenses = relationship("Expense", back_populates="owner")  # связь с расходами

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String(64), nullable=False)
    description = Column(String(255))
    date = Column(DateTime, server_default=func.now(), nullable=False)  # автоматически проставляется
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # внешний ключ
    owner = relationship("User", back_populates="expenses")

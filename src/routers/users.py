from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas import UserCreate, UserOut
from src.models import User
from src.crud import create_user, verify_password
from src.db import get_db
from src.auth import create_access_token, get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_in.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    new_user = create_user(db, user_in.email, user_in.password)
    return new_user

@router.post("/login", status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token_data = {"sub": user.email}
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

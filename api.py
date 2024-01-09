from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from models import User
from schemas import UserCreate, UserOut
from db import get_db


router = APIRouter(
    prefix= "/api/users",
    tags=["users"],
)


@router.get("/",response_model=List[UserOut])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/{id}", response_model=UserOut)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    return user


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import tables
import schemas
from database import get_db

router = APIRouter()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.User_response)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hashing the password
    user.password = pwd_context.hash(user.password)
    new_user = tables.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(tables.Users).filter(tables.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

@router.get("/users")
def get_allusers(db: Session = Depends(get_db)):
    users =  db.query(tables.Users).all()
    return users
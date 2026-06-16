from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import tables
import schemas,ouath2
import utils
from database import get_db

router = APIRouter()

@router.post("/login")
def login(creds: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(tables.Users).filter(tables.Users.email == creds.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    access_token = ouath2.create_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

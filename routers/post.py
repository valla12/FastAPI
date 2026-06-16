from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import tables
import schemas
from database import get_db

router = APIRouter()


@router.get("/post")
def post(db: Session = Depends(get_db)):
    posts = db.query(tables.Post).all()
    return {'data': posts}


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create(data: schemas.PostCreate, db: Session = Depends(get_db)):
    # This is a cleaner way to unpack the dictionary
    new_post = tables.Post(**data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"data": new_post}


@router.get('/post/{id}')
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(tables.Post).filter(tables.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    return {'found post': post}

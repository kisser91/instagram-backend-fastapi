from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix="/users",tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # Hash the password - user.password
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass
    new_user = models.User(**user.dict()) ## **
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model= List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    # REGULAR POSTGRESQL and PSYCOPG
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()

    # SQLALCHEMY ORM
    users =db.query(models.User).all()
    return users   

@router.get("/{id}", response_model= schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    # REGULAR POSTGRESQL and PSYCOPG
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()

    # SQLALCHEMY ORM
    user =db.query(models.User).filter(models.User.id == id).first()  
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")
    print(user.id)
    return user 
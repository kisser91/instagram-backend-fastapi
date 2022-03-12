from logging import raiseExceptions
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from .. import oauth2
from typing import Optional

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # REGULAR POSTGRESQL and PSYCOPG
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # SQLALCHEMY ORM
    print(limit)
    posts =db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.get("/{id}", response_model= schemas.Post)
def get_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # REGULAR POSTGRESQL and PSYCOPG
    # cursor.execute(""" SELECT * from posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    # SQLALCHEMY ORM
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # REGULAR POSTGRESQL and PSYCOPG
    ## protect the db from SQLINYECTION
    # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content, post.published))
    # new_post= cursor.fetchone()
    # conn.commit()
    
    # SQLALCHEMY ORM
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.put("/{id}", response_model= schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # SQLALCHEMY ORM
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    print(post)

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
    
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # REGULAR POSTGRESQL and PSYCOPG
    # cursor.execute(""" DELETE FROM posts WHERE id = %s returning *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    # SQLALCHEMY ORM
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    if current_user.id != post.owner_id:
        print(current_user.id == post.owner_id)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT)


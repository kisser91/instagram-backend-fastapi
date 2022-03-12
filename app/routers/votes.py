from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas,database,models,oauth2

router = APIRouter(
    prefix="/vote",
    tages="Vote"
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote():
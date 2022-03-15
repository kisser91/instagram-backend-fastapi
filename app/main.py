from fastapi import FastAPI
from . import models
from .database import Base, engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# db Models
# models.Base.metadata.create_all(bind=engine)


# Main execution 
app = FastAPI()
origins = ["www.example-web.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Hello World"}


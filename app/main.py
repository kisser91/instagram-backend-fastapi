from fastapi import FastAPI
from . import models
from .database import Base, engine
from .routers import post,user,auth
from .config import settings

# db Models
models.Base.metadata.create_all(bind=engine)

# Main execution 
app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Hello World"}


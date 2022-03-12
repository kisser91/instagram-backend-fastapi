from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


## legacy, we dint use this anymore


# while True:
#     try:
#         conn = psycopg2.connect(host ='localhost',database='fasapi',user='postgres',password='kornero07', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succefull!")
#         break
#     except Exception as error:
#         print("Connection do database failed")
#         print("Error: ", error)
#         time.sleep(2)
        


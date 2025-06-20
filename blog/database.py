from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
SQLALCHAMY_DATABASE_URL= "postgresql://postgres:anto1412@localhost:5432/bookstore"

engine = create_engine(SQLALCHAMY_DATABASE_URL)
    
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()  
    try:
        yield db  
    finally:
        db.close() 

# def create_table():
#     Base.metadata.create_all(bind=engine) 
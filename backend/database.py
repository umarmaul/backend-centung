from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:WqD03avKX8BfewcTtyQDGbuSBmD0gnJ3JV9XQ7ORlBoAg1hYGLNUCZ9qL7OLmN3P@145.223.117.210:5432/centung"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
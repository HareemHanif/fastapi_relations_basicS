from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv('POSTGRES_USER','postgres')
DB_PASS = os.getenv('POSTGRES_PASSWORD','postgres')
DB_NAME = os.getenv('POSTGRES_DB','fastapidb')
DB_HOST = os.getenv('POSTGRES_HOST','db')
DB_PORT = os.getenv('POSTGRES_PORT','5432')

PASSWORD = quote_plus(DB_PASS)
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

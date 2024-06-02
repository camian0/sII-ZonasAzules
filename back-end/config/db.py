from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.configEnv import ENGINE, USER, PASSWORD, HOST, DBNAME


SQLALCHEMY_DATABASE_URL = f"{ENGINE}://{USER}:{PASSWORD}@{HOST}/{DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

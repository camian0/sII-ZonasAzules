from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.ConfigEnv import ENGINE, USER, PASSWORD, HOST, DBNAME


SQLALCHEMY_DATABASE_URL = f"{ENGINE}://{USER}:{PASSWORD}@{HOST}/{DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

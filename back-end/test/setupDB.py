from models.meta import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.configEnv import ENGINE, USER, PASSWORD, HOST, TESTDBNAME

SQLALCHEMY_DATABASE_URL = f"{ENGINE}://{USER}:{PASSWORD}@{HOST}/{TESTDBNAME}"

__engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=__engine)

Base.metadata.drop_all(bind=__engine)
Base.metadata.create_all(bind=__engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

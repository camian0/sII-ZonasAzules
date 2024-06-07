from dotenv import load_dotenv
import os

load_dotenv()

ENGINE = os.getenv("engine")
USER = os.getenv("user")
PASSWORD = os.getenv("pass")
HOST = os.getenv("host")
DBNAME = os.getenv("db_name")
SECRET = os.getenv("secret")
TESTDBNAME = os.getenv("testDbName")

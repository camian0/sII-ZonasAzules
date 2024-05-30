import os
from dotenv import load_dotenv
import configparser


# load environment variables
load_dotenv()

# load enviroment variables on local variables
engine = os.getenv("engine")
user = os.getenv("user")
passw = os.getenv("pass")
host = os.getenv("host")
dbName = os.getenv("db_name")

database_url = f"{engine}://{user}:{passw}@{host}/{dbName}"


# Cargar el archivo alembic.ini
config = configparser.ConfigParser()
config.read("alembic.ini")


# Actualizar sqlalchemy.url con la variable de entorno
config["alembic"]["sqlalchemy.url"] = database_url

# Guardar los cambios en alembic.ini
with open("alembic.ini", "w") as configfile:
    config.write(configfile)

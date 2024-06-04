import configparser
from configEnv import ENGINE, USER, PASSWORD, HOST, DBNAME


database_url = f"{ENGINE}://{USER}:{PASSWORD}@{HOST}/{DBNAME}"


# Cargar el archivo alembic.ini
config = configparser.ConfigParser()
config.read("alembic.ini")


# Actualizar sqlalchemy.url con la variable de entorno
config["alembic"]["sqlalchemy.url"] = database_url

# Guardar los cambios en alembic.ini
with open("alembic.ini", "w") as configfile:
    config.write(configfile)

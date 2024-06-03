import logging
from datetime import datetime

# Obtener la fecha actual y formatearla
current_date = datetime.now().strftime("%Y-%m-%d")

# Configuración básica del logging con el nombre del archivo basado en la fecha actual
logging.basicConfig(
    filename=f"./logs/{current_date}.log",  # Nombre del archivo de log basado en la fecha actual
    filemode="a",  # Modo de apertura del archivo: 'a' para append, 'w' para overwrite
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato del mensaje de log
    level=logging.INFO,  # Nivel de log: DEBUG, INFO, WARNING, ERROR, CRITICAL
)

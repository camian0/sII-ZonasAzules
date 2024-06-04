from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])


def verifyPassword(textPassword: str, hashedPassword: str) -> bool | None:
    """
    Metodo para verificar la contraseña ingresada por el usuario y el hash almacenado en la base de datos

    Args:
        textPassword (str): Contraseña ingresada por el usuario
        hashedPassword (str): Hash de la contraseña almacenado en la base de datos

    Returns:
        bool | None: Devuelve verdadero si las contraseñas coinciden, o si alguno de los parametros no fueron ingresados devuelve un None
    """
    res = None
    if textPassword != None and hashedPassword != None:
        res = pwd_context.verify(textPassword, hashedPassword)
    return res


def getPasswordHash(password: str) -> str | None:
    """
    Obtiene un hash de alguna cadena de texto ingresada

    Args:
        password (str): Cadena de texto a cifrar

    Returns:
        str | None: Devuelve el hash generado con el algoritmo sha256 o None si no se ingreso ninguna cadena de texto
    """
    hash = None
    if password != None:
        hash = pwd_context.hash(password)
    return hash

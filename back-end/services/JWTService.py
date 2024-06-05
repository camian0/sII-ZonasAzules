from jwt import encode, decode
from config.ConfigEnv import SECRET


def encodeJwt(data: dict) -> str | None:
    """
    Metodo para generar un token jwt con un diccionario recibido

    Args:
        data (dict): Diccionario con los datos del usuario que quiere iniciar sesion

    Returns:
        str | None: Devuelve el token generado, si ocurre un error en la generación de este, devuelve un None
    """
    if data:
        token: str = encode(payload=data, key=SECRET, algorithm="HS256")
        return token
    return None


def decodeJwt(token: str) -> dict | None:
    """
    Metodo para decodificar un token enviado por la peticion al backend

    Args:
        token (str): Token que se envía por la peticion y decodifica la informacion que contiene

    Returns:
        dict | None: Devuelve la informacion contenida en el token decodificada, para hacer verificacions posteriores,
        si hay algun error en la decodificación no devuelve nada
    """
    if token:
        data: dict = decode(jwt=token, key=SECRET, algorithms=["HS256"])
        return data

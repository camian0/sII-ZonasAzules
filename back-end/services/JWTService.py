from jwt import encode, decode
from config.ConfigEnv import SECRET


def hola():
    print("hola mundo")


def encodeJwt(data: dict):
    token: str = encode(payload=data, key=SECRET, algorithm="HS256")
    return token


def decodeJwt(token: str) -> dict:
    data: dict = decode(jwt=token, key=SECRET, algorithms=["HS256"])
    return data

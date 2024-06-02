from jwt import encode, decode
from config.configEnv import SECRET


def encodeJwt(data: dict) -> str | None:
    if data:
        token: str = encode(payload=data, key=SECRET, algorithm="HS256")
        return token
    return None


def decodeJwt(token: str) -> dict | None:
    if token:
        data: dict = decode(jwt=token, key=SECRET, algorithms=["HS256"])
        return data

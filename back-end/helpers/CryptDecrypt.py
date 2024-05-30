from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])


def verifyPassword(textPassword: str, hashedPassword: str) -> bool | None:
    res = None
    if textPassword != None and hashedPassword != None:
        res = pwd_context.verify(textPassword, hashedPassword)
    return res


def getPasswordHash(password: str) -> str | None:
    hash = None
    if password != None:
        hash = pwd_context.hash(password)
    return hash

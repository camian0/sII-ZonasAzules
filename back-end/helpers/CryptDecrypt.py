from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])


def verifyPassword(textPassword: str, hashedPassword: str) -> bool:
    return pwd_context.verify(textPassword, hashedPassword)


def getPasswordHash(password: str) -> str:
    return pwd_context.hash(password)

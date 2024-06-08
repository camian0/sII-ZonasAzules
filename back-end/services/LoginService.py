from sqlalchemy.orm import Session

from helpers.CryptDecrypt import verifyPassword
from models.authUser import AuthUser
from models.user import User
from schemas.UserAuthSchema import UserAuthSchema
from services.JWTService import encodeJwt


def login(userAuth: UserAuthSchema, db: Session) -> str | None:
    """
    Iniciar sesion en el sistema, si el usuario y la contraseña enviados son correctos

    Args:
        userAuth (UserAuthSchema): Modelo con los campos requeridos para el inicio de sesion, que se reciben en la peticion hecha al endpont
        db (Session): sesion de la base de datos que se envia desde el endpoint que se llamó

    Returns:
        str | None: devuelve un token jwd como autenticacion exitosa
    """
    query = db.query(AuthUser).filter(userAuth.email == AuthUser.email).first()
    if query:
        if verifyPassword(userAuth.password, query.password):
            delattr(userAuth, "password")
            userAuth.role_id = query.role_id

            token = encodeJwt(userAuth.__dict__)
            return token
    return None


def createAuthUser(user: AuthUser, db: Session) -> bool:
    """
    Crea un usuario que es el que se va a autenticar en el sistema

    Args:
        user (AuthUser): Modelo con los campos requeridos para iniciar sesion, se envia el modelo ya creado y validados desde la creacion del usuario
        db (Session): Sesion de la base de datos que se envia desde el endpoint que se llamó

    Returns:
        bool: Devuelve un valor booleano si se creo correctamente el authUser
    """

    if user:
        db.add(user)
        db.commit()
        db.refresh(user)
        return True
    return False

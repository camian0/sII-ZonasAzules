from typing import List
from sqlalchemy.orm import Session

from models.user import User
from models.authUser import AuthUser
from schemas.User import UserSchema
from helpers.CryptDecrypt import getPasswordHash
from services.LoginService import createAuthUser
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import (
    USER_ALREARY_EXIST,
    CREATED_USER_OK,
    GET_ALL_USERS_TYPE_OK,
)
from helpers.dtos.responseDto import ResponseDto
from helpers.helpers import queryPaginate


def getUsers(page, sizePage, db: Session) -> ResponseDto:
    """
    Método para obtener todos los usuarios(perfiles) del sistema

    Args:
        db (Session): sesion de la base de datos

    Returns:
        List[User] | None: El método devuelve una lista de objetos de tipo usuario, objetos de tipo clave valor
    """
    responseDto = ResponseDto()

    query = db.query(User)
    res = queryPaginate(query, page, sizePage)

    users = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_USERS_TYPE_OK
    responseDto.data = users
    return responseDto


def create(user: UserSchema, db: Session) -> bool:
    """
    Método para agregar un user y authUser en un mismo flujo, los datos creados del usuario son agregados
    para el modelo de auth user, si se guardan exitosamente los dos se hace el commit a la base de datos
    de lo contrario, se hace un rollback.
    Si ocurre un error inesperado también devuelve toda la transaccion a la base de datos con rollback

    Args:
        user (UserSchema): datos del usuario que van a ser guardados, y que están agrupados en userSchema
        db (Session): sesion de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        bool: Devuelve una confirmacion de verdadero o falso si se lograron guardar ambos usuarios
    """
    newUser = User()
    newUser.__dict__.update(user.__dict__)
    newAuthUser = AuthUser()
    passwordHash = getPasswordHash(newUser.password)
    newAuthUser.email = newUser.email
    newAuthUser.password = passwordHash
    # TODO cambiarlo para recibirlo del front
    newAuthUser.role_id = 2
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    newAuthUser.user_id = newUser.id
    result = createAuthUser(newAuthUser, db)
    if not result:
        db.rollback()
        return False

    return True

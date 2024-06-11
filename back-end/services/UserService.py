from typing import List
from sqlalchemy.orm import Session

from models.user import User
from models.authUser import AuthUser
from schemas.userSchema import UserSchema
from helpers.CryptDecrypt import getPasswordHash
from services.LoginService import createAuthUser
from helpers.statusCodes import OK, FORBIDEN
from helpers.responseMessages import GET_ALL_USERS_TYPE_OK, CREATED_USER_OK, USER_NOT_CREATED
from helpers.dtos.responseDto import ResponseDto
from helpers.helpers import queryPaginate


def getUsers(page, sizePage, db: Session) -> ResponseDto:
    """
    Método para obtener todos los usuarios(perfiles) del sistema

    Args:
        db (Session): sesion de la base de datos

    Returns:
        ResponseDto: El método devuelve una lista de objetos de tipo usuario, objetos de tipo clave valor
    """
    responseDto = ResponseDto()

    query = db.query(User)
    res = queryPaginate(query, page, sizePage)

    users = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_USERS_TYPE_OK
    responseDto.data = users
    return responseDto


def create(user: UserSchema, db: Session) -> ResponseDto:
    """
    Método para agregar un user y authUser en un mismo flujo, los datos creados del usuario son agregados
    para el modelo de auth user, si se guardan exitosamente los dos se hace el commit a la base de datos
    de lo contrario, se hace un rollback.
    Si ocurre un error inesperado también devuelve toda la transaccion a la base de datos con rollback

    Args:
        user (UserSchema): datos del usuario que van a ser guardados, y que están agrupados en userSchema
        db (Session): sesion de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: Devuelve un objeto response con la informacion de la transaccion
    """
    newUser = User()
    response = ResponseDto()
    newUser.__dict__.update(user.__dict__)
    newAuthUser = AuthUser()
    passwordHash = getPasswordHash(newUser.password)
    newAuthUser.email = newUser.email
    newAuthUser.password = passwordHash
    newAuthUser.role_id = newUser.role_id
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    newAuthUser.user_id = newUser.id
    result = createAuthUser(newAuthUser, db)
    if not result:
        db.rollback()
        response.status=FORBIDEN
        response.message=USER_NOT_CREATED
        return response

    response.status=OK
    response.message=CREATED_USER_OK
    response.data= newUser.dict();
    return response

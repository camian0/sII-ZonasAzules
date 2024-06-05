from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, Request

from .JWTService import decodeJwt
from sqlalchemy.orm import Session
from config.dB import getDb

from typing import List
from sqlalchemy.orm import Session
from models.creditCard import CreditCard
from schemas.CreditCardSchema import CreditCardSchema
from helpers.helpers import listRelationship

class CardService(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(getDb)):
        credentials = await super().__call__(request)
        reqBody = credentials.credentials
        if reqBody.__contains__('"'):
            reqBody = reqBody.replace('"', "")
        data = decodeJwt(reqBody)
        '''
        
        if data:
            user = db.query(CreditCard).filter(AuthUser.email == data["email"]).first()
            if user:
                return credentials
            else:
                raise HTTPException(
                    status_code=403, detail="Invalid authorization code"
                )
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
        '''

def getCreditCard(db: Session) -> List[CreditCard] | None:
    """
    Método para obtener todos las tarjetas de crédito del sistema

    Args:
        db (Session): sesion de la base de datos

    Returns:
        List[CreditCard] | None: El método devuelve una lista de objetos de tipo tarjeta de credito, 
        objetos de tipo clave valor
    """
    query = db.query(CreditCard).all()
    if len(query) > 0:
        card = [i.dict() for i in query]
        return card
    return None

'''
def create(user: CreditCardSchema, db: Session) -> bool:
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
'''
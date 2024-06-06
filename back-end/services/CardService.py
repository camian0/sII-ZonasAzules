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



def get(db: Session) -> List[CreditCard] | None:
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
        cards = [i.dict() for i in query]
        return cards
    return None


def create(creditCardSchema: CreditCardSchema, db: Session) -> CreditCard:
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
    newCard = CreditCard()
    newCard.__dict__.update(creditCardSchema.__dict__)
    db.add(newCard)
    db.commit()
    db.refresh(newCard)
    return newCard

from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, Request

from .JWTService import decodeJwt
from sqlalchemy.orm import Session
from config.dB import getDb

from typing import List
from sqlalchemy.orm import Session
from models.creditCard import CreditCard
from schemas.CreditCardSchema import CreditCardSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.helpers import queryPaginate
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import CREDIT_CARD_ALREARY_EXIST, CREATED_CREDIT_CARD_OK, GET_ALL_CREDIT_CARD_OK, NOT_FOUND_CREDIT_CARD, DELETED_CREDIT_CARD_OK, FOUND_CREDIT_CARD_OK, NOT_FOUND_CREDIT_CARD_BY_ID



def get(db: Session, page: int, sizePage: int) -> ResponseDto:
    responseDto = ResponseDto()
    query = db.query(CreditCard)
    res = queryPaginate(query, page, sizePage)
    
    cards = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_CREDIT_CARD_OK
    responseDto.data = cards
    return responseDto


def getByNumber(creditCardNumber: str, db: Session) -> ResponseDto:
    """
    Método para obtener una Tarjeta de crédito por el número
    Args:
        creditCardNumber (str): número de la tarjeta de crédito a buscar
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    print("ESTOY CANSADO")
    existCreditCard = db.query(CreditCard).filter_by(number=creditCardNumber).first()
    if not existCreditCard:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_CREDIT_CARD
        return responseDto
    
    responseDto.status = OK
    responseDto.message = GET_ALL_CREDIT_CARD_OK
    responseDto.data = existCreditCard.dict()
    return responseDto

def getByUserId(id: int, db: Session) -> ResponseDto:
    """
    Método para obtener las zonas dado el id del area
    Args:
        id (int): número del area a buscar
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    
    responseDto = ResponseDto()
    existCard = db.query(CreditCard).filter_by(user_id = id).all()
    print(existCard)
    if not existCard:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_CREDIT_CARD_BY_ID
        return responseDto
    
    cards = [i.dict() for i in existCard]
    responseDto.status = OK
    responseDto.message = GET_ALL_CREDIT_CARD_OK
    responseDto.data = cards
    return responseDto
    
'''
def getByIdUser(id: int, db: Session, page: int = 1, sizePage: int = 10) -> ResponseDto:
    """
    Método para obtener una Tarjeta de crédito por el id de usuario
    Args:
        id (str): id del usuario
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    query = db.query(CreditCard).filter_by(user_id=id)
    res = queryPaginate(query, page, sizePage)

    if not res:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_CREDIT_CARD
        return responseDto

    
    creditCard = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_CREDIT_CARD_OK
    responseDto.data = creditCard
    return responseDto
'''

def create(creditCardSchema: CreditCardSchema, db: Session) -> ResponseDto:
    """
    Método para crear una Tarjeta de crédito
    Args:
        creditCardSchema (CreditCardSchema): esquema que contiene los datos para la creación 
        de la tarjeta de crédito.
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existCreditCard = db.query(CreditCard).filter_by(number=creditCardSchema.number).first()
    if existCreditCard:
        responseDto.status = BAD_REQUEST
        responseDto.message = CREDIT_CARD_ALREARY_EXIST
        return responseDto
    
    newCreditCard = CreditCard(**creditCardSchema.__dict__)
    db.add(newCreditCard)
    db.commit()
    db.refresh(newCreditCard)

    responseDto.status = OK
    responseDto.message = CREATED_CREDIT_CARD_OK
    responseDto.data = newCreditCard.dict()
    return responseDto

def delete(creditCardNumber: str, db: Session) -> ResponseDto:
    """
    Método para eliminar una Tarjeta de crédito
    Args:
        creditCardNumber (CreditCardSchema): esquema que contiene los datos para la eliminación 
        de la tarjeta de crédito.
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    creditCard = db.query(CreditCard).filter_by(number=creditCardNumber).first()
    if not creditCard:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_CREDIT_CARD
        return responseDto

    db.delete(creditCard)
    db.commit()

    responseDto.status = OK
    responseDto.message = DELETED_CREDIT_CARD_OK
    responseDto.data = creditCard.dict()
    return responseDto
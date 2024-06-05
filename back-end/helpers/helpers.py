from typing import List, TypeVar
from sqlalchemy.orm import Query

T = TypeVar("T")  # Definimos un tipo genérico


# sacar todos los elementos de una relacion en dict y devolver esa lista
def listRelationship(relation: List[T]) -> List[dict]:
    """
    Funcion que recibe una lista de relaciones tipo T y que devuelve una lista
    de relaciones de objetos dict

    Args:
        relation (List[T]): Una lista de objetos tipo T(authUser, user, roles) que son modelos de sqlalquemy

    Returns:
        List[T]: devuelve una lista de objetos T(authUser, user, roles) serializables para devolverlos
        en un arreglo json
    """
    list = []
    for item in relation:
        list.append(item.dict())
    return list


"""ejemplo
for item in query:
            obj = item.dict()
            auth_users = __listRelationship(item.auth_users)
            credit_cards = __listRelationship(item.credit_cards)
            reservations = __listRelationship(item.reservations)
            obj["auth_users"] = auth_users
            obj["credit_cards"] = credit_cards
            obj["reservations"] = reservations
            users.append(obj)


"""


def queryPaginate(query: T, page: int, sizePage: int) -> Query[T]:
    """
    Método para páginar una consulta a la base de datos

    Args:
        query (T): Una consulta
        page (int): Página de inicio
        sizePage (int): Registros devueltos por página

    Returns:
        Query[T]: Devuelve una consulta con el numero de registros recibidos por parámetros
    """
    count = query.count()
    if page < 0:
        page = 1
    if sizePage > count:
        sizePage = count
    res = query.limit(sizePage).offset(sizePage * (page - 1)).all()
    return res

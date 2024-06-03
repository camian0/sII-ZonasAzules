from typing import List, TypeVar

T = TypeVar("T")  # Definimos un tipo genérico


# sacar todos los elementos de una relacion en dict y devolver esa lista
def listRelationship(relation: List[T]) -> List[T]:
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

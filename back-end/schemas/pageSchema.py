from pydantic import BaseModel


class PageSchema(BaseModel):
    """
    Esquema page para el manejo mas facil de la páginacion cuando se quere obtener muchos los registros de una tabla.
    Posee dos valores por defecto, numero de página de inicio(page) y numero de registros por página (sizePage)

    """

    page: int = 1
    sizePage: int = 10

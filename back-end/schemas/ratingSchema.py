from pydantic import BaseModel
from pydantic import field_validator


class RatingSchema(BaseModel):
    observation: str
    rating: int

    @field_validator("rating")
    def passwordName(cls, rating):

        if len(rating) < 0:
            raise ValueError("La calificacion mínima es de 0 puntos.")
        if len(rating) > 5:
            raise ValueError("La calificación maxima es de 5 puntos.")

        return rating

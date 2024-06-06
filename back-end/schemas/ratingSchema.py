from pydantic import BaseModel
from pydantic import field_validator


class RatingSchema(BaseModel):
    observation: str
    qualification: int
    blue_zone_id: int

    @field_validator("qualification")
    def qualificationValidation(cls, qualification):

        if qualification < 0:
            raise ValueError("La calificacion mínima es de 0 puntos.")
        if qualification > 5:
            raise ValueError("La calificación maxima es de 5 puntos.")

        return qualification

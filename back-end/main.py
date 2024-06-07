import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes.AuthRoute import authRoute
from routes.UserRoute import userRoutes
from routes.CardRoute import cardRoutes
from routes.blueZoneRoute import blueZoneRoute
from routes.areaRoute import areaRoutes
from routes.ratingRoute import ratingRoute
from routes.placeTypeRoute import placeTypeRoute
from routes.reservationRoute import reservationRoute
from routes.reportRoute import reportRoutes
from schemas.exceptions.validationExceptionHandler import validation_exception_handler


app = FastAPI()
# Registra el manejador de excepciones
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(authRoute)
app.include_router(userRoutes)
app.include_router(cardRoutes)

app.include_router(blueZoneRoute)
app.include_router(areaRoutes)
app.include_router(ratingRoute)
app.include_router(placeTypeRoute)
app.include_router(reservationRoute)
app.include_router(reportRoutes)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
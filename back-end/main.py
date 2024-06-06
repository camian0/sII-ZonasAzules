import uvicorn
from fastapi import FastAPI

from routes.AuthRoute import authRoute
from routes.UserRoute import userRoutes
from routes.blueZoneRoute import blueZoneRoute
from routes.areaRoute import areaRoutes
from routes.placeTypeRoute import placeTypeRoute
from routes.reservationRoute import reservationRoute


app = FastAPI()
app.include_router(authRoute)
app.include_router(userRoutes)
app.include_router(blueZoneRoute)
app.include_router(areaRoutes)
app.include_router(placeTypeRoute)
app.include_router(reservationRoute)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

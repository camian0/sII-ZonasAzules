import uvicorn
from fastapi import FastAPI

from routes.AuthRoute import authRoute
from routes.UserRoute import userRoutes
from routes.blueZoneRoute import blueZoneRoute


app = FastAPI()
app.include_router(authRoute)
app.include_router(userRoutes)
app.include_router(blueZoneRoute)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

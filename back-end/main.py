from fastapi import FastAPI

from routes.AuthRoute import authRoute
from routes.UserRoute import userRoutes


app = FastAPI()
app.include_router(authRoute)
app.include_router(userRoutes)


@app.get("/")
def read_root():
    return {"Hello": "World"}

from typing import Union
from dotenv import load_dotenv
from models import Base


from fastapi import FastAPI
from routers.searchBlueZoneRouter import search_blue_zone_router
import os

# load environment variables
load_dotenv()

app = FastAPI()

app.include_router(search_blue_zone_router)
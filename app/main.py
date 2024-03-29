import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import api, config

logging.basicConfig()    
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)
app = FastAPI(debug=config.DEBUG, title="Mura")
app.mount("/", StaticFiles(directory="public", html=True))
app.include_router(api.router)

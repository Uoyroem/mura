from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import config, api

app = FastAPI(debug=config.DEBUG, title="Mura")
app.mount("/", StaticFiles(directory="public", html=True))
app.include_router(api.router)

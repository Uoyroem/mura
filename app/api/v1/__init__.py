from fastapi import APIRouter
from . import auth, users

router = APIRouter(prefix="/v1")
router.include_router(auth.router)
router.include_router(users.router)

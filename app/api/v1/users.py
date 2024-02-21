from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("/profile")
async def profile():
    pass

from fastapi import APIRouter
from fastapi.responses import RedirectResponse
router = APIRouter()

@router.get("/api/docs")
async def documentation():
    return RedirectResponse("/docs")
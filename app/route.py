from fastapi import APIRouter
from app.routers import auth_routes, shift_allowance_routes

router = APIRouter()

router.include_router(auth_routes.router,tags=["Authentication"])
router.include_router(shift_allowance_routes.router,tags=["Operations"])
from fastapi import APIRouter,Depends,BackgroundTasks
from schemas.userschema import UserCreate, UserResponse
from schemas.authschema import LoginRequest,RefreshTokenRequest
from services.auth_service import register_user,authenticate_user,register_admin_user,refresh_access_token  # logic in services
from sqlalchemy.orm import Session
from db import get_db
router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate,db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return authenticate_user(db, request.email, request.password)

@router.post("/register/admin", response_model=UserResponse)
def register_admin(user: UserCreate, db: Session = Depends(get_db)):
    return register_admin_user(db, user)


@router.post("/refresh")
async def refresh_token(request: RefreshTokenRequest):
    return refresh_access_token(request.refresh_token)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    Token,
)

from app.services.user_service import UserService

from app.core.dependencies import get_current_user

from app.models.users import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return UserService.register(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    
@router.post(
    "/login",
    response_model=Token,
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):

    try:

        return UserService.login(
            db,
            user.email,
            user.password,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):

    return current_user
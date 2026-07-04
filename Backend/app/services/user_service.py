from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.users import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class UserService:

    @staticmethod
    def register(
        db: Session,
        user_data: UserCreate,
    ):

        existing_user = UserRepository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise ValueError(
                "Email already registered"
            )

        user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            ),
        )

        return UserRepository.create(
            db,
            user,
        )
    
    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = UserRepository.get_by_email(
            db,
            email,
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.core.dependencies import get_current_user
from app.models.users import User
from app.services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.get("/summary/{report_id}")
def executive_summary(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return AIService.executive_summary(
        db,
        report_id,
    )
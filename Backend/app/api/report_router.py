from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.db import get_db
from app.models.users import User
from app.schemas.report import ReportResponse
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post(
    "/import",
    response_model=list[ReportResponse],
)
def import_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ReportService.import_reports(db)


@router.get(
    "",
    response_model=list[ReportResponse],
)
def get_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ReportService.get_all(db)


@router.get(
    "/{report_id}",
    response_model=ReportResponse,
)
def get_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:
        return ReportService.get_by_id(
            db,
            report_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{report_id}",
)
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        ReportService.delete(
            db,
            report_id,
        )

        return {
            "message": "Report deleted successfully"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

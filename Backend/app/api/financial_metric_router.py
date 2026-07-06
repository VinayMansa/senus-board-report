from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.db import get_db
from app.models.users import User
from app.schemas.financial_metric import (
    FinancialMetricResponse,
)
from app.services.financial_metric_service import (
    FinancialMetricService,
)

router = APIRouter(
    prefix="/metrics",
    tags=["Financial Metrics"],
)


@router.get(
    "/{report_id}",
    response_model=list[FinancialMetricResponse],
)
def get_metrics(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return FinancialMetricService.get_metrics(
        db,
        report_id,
    )


@router.delete("/{report_id}")
def delete_metrics(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    FinancialMetricService.delete_metrics(
        db,
        report_id,
    )

    return {
        "message": "Metrics deleted successfully"
    }
@router.post("/process/{report_id}")
def process_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        metrics = FinancialMetricService.process_report(
            db,
            report_id,
        )

        return {
            "message": "Report processed successfully",
            "metrics_extracted": len(metrics),
            "metrics": metrics,
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
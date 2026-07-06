from sqlalchemy.orm import Session

from app.models.financial_metric import FinancialMetric
from app.repositories.financial_metric_repository import (
    FinancialMetricRepository,  # pyright: ignore[reportAttributeAccessIssue]
)


class FinancialMetricService:

    @staticmethod
    def create_metric(
        db: Session,
        report_id: int,
        metric_name: str,
        metric_value: float,
        unit: str = "",
        page_number: int | None = None,
    ):

        metric = FinancialMetric(
            report_id=report_id,
            metric_name=metric_name,
            metric_value=metric_value,
            unit=unit,
            page_number=page_number,
        )

        return FinancialMetricRepository.create(
            db,
            metric,
        )

    @staticmethod
    def get_metrics(
        db: Session,
        report_id: int,
    ):
        return FinancialMetricRepository.get_by_report(
            db,
            report_id,
        )

    @staticmethod
    def delete_metrics(
        db: Session,
        report_id: int,
    ):
        FinancialMetricRepository.delete_by_report(
            db,
            report_id,
        )
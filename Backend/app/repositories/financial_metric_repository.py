from sqlalchemy.orm import Session

from app.models.financial_metric import FinancialMetric


class FinancialMetricRepository:

    @staticmethod
    def create(
        db: Session,
        metric: FinancialMetric,
    ):
        db.add(metric)
        db.commit()
        db.refresh(metric)
        return metric

    @staticmethod
    def create_many(
        db: Session,
        metrics: list[FinancialMetric],
    ):
        db.add_all(metrics)
        db.commit()

    @staticmethod
    def get_by_report(
        db: Session,
        report_id: int,
    ):
        return (
            db.query(FinancialMetric)
            .filter(
                FinancialMetric.report_id == report_id
            )
            .all()
        )

    @staticmethod
    def delete_by_report(
        db: Session,
        report_id: int,
    ):
        (
            db.query(FinancialMetric)
            .filter(
                FinancialMetric.report_id == report_id
            )
            .delete()
        )

        db.commit()
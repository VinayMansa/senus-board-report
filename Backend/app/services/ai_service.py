from sqlalchemy.orm import Session

from app.models.financial_metric import FinancialMetric
from app.ai.summary_generator import SummaryGenerator


class AIService:

    @staticmethod
    def executive_summary(
        db: Session,
        report_id: int,
    ):

        metrics = (
            db.query(FinancialMetric)
            .filter(
                FinancialMetric.report_id == report_id
            )
            .all()
        )

        return {
            "summary":
            SummaryGenerator.generate(metrics)
        }
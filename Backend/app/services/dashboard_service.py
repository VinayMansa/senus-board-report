from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.report import Report
from app.models.financial_metric import FinancialMetric


class DashboardService:

    @staticmethod
    def summary(db: Session):

        total_reports = db.query(Report).count()

        processed_reports = (
            db.query(Report)
            .filter(Report.status == "Processed")
            .count()
        )

        pending_reports = (
            db.query(Report)
            .filter(Report.status == "Pending")
            .count()
        )

        total_metrics = db.query(FinancialMetric).count()

        companies = (
            db.query(func.count(func.distinct(Report.company_name)))
            .scalar()
        )

        return {
            "total_reports": total_reports,
            "processed_reports": processed_reports,
            "pending_reports": pending_reports,
            "total_metrics": total_metrics,
            "companies": companies,
        }

    @staticmethod
    def reports(db: Session):

        reports = db.query(Report).all()

        result = []

        for report in reports:

            metric_count = (
                db.query(FinancialMetric)
                .filter(
                    FinancialMetric.report_id == report.id
                )
                .count()
            )

            result.append(
                {
                    "id": report.id,
                    "title": report.title,
                    "company": report.company_name,
                    "year": report.financial_year,
                    "status": report.status,
                    "metrics": metric_count,
                }
            )

        return result

    @staticmethod
    def report_details(
        db: Session,
        report_id: int,
    ):

        report = (
            db.query(Report)
            .filter(
                Report.id == report_id
            )
            .first()
        )

        if report is None:
            return None

        metrics = (
            db.query(FinancialMetric)
            .filter(
                FinancialMetric.report_id == report_id
            )
            .all()
        )

        return {
            "report": report,
            "metrics": metrics,
        }

    @staticmethod
    def kpis(
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
            metric.metric_name: metric.metric_value
            for metric in metrics
        }
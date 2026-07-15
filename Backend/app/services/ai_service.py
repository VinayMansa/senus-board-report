from sqlalchemy.orm import Session

from app.models.report import Report
from app.models.financial_metric import FinancialMetric

from app.ai.llm import LLM


class AIService:

    @staticmethod
    def executive_summary(
        db: Session,
        report_id: int,
    ):

        report = (
            db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

        if report is None:
            raise ValueError("Report not found")

        metrics = (
            db.query(FinancialMetric)
            .filter(
                FinancialMetric.report_id == report_id
            )
            .all()
        )

        if not metrics:
            raise ValueError(
                "No financial metrics found for this report."
            )

        metric_lines = []

        for metric in metrics:

            metric_lines.append(
                f"{metric.metric_name}: {metric.metric_value}"
            )

        metrics_text = "\n".join(metric_lines)

        prompt = f"""
Company: {report.company_name}

Report Type: {report.report_type}

Financial Year: {report.financial_year}

Financial Metrics

{metrics_text}

Generate a professional executive summary for a Board of Directors.

Requirements:

- Maximum 250 words.
- Mention financial performance.
- Mention profitability.
- Mention strengths.
- Mention weaknesses.
- Mention business risks.
- Mention recommendations.
- Use a professional tone.
- Do not invent financial numbers.
"""

        summary = LLM.generate(prompt)

        return {
            "company": report.company_name,
            "year": report.financial_year,
            "summary": summary,
        }
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.base import Base


class FinancialMetric(Base):

    __tablename__ = "financial_metrics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    report_id: Mapped[int] = mapped_column(
        ForeignKey("reports.id"),
        nullable=False,
    )

    metric_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    metric_value: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
    )

    page_number: Mapped[int] = mapped_column(
        Integer,
        nullable=True,
    )

    extracted_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
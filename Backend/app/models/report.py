from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    company_name: Mapped[str] = mapped_column(String(255), nullable=False)

    report_type: Mapped[str] = mapped_column(String(100), nullable=False)

    financial_year: Mapped[int] = mapped_column(Integer, nullable=False)

    source_url: Mapped[str] = mapped_column(String(1000), nullable=False)

    file_name: Mapped[str] = mapped_column(String(255), nullable=True)

    local_path: Mapped[str] = mapped_column(String(500), nullable=True)

    status: Mapped[str] = mapped_column(
        String(50),
        default="Pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
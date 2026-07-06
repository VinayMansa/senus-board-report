from sqlalchemy.orm import Session

from app.models.report import Report


class ReportRepository:

    @staticmethod
    def create(db: Session, report: Report):
        db.add(report)
        db.commit()
        db.refresh(report)
        return report

    @staticmethod
    def get_all(db: Session):
        return db.query(Report).all()

    @staticmethod
    def get_by_id(db: Session, report_id: int):
        return (
            db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

    @staticmethod
    def delete(db: Session, report: Report):
        db.delete(report)
        db.commit()
    @staticmethod
    @staticmethod
    def update(
        db: Session,
        report: Report,
    ):
        db.commit()
        db.refresh(report)
        return report
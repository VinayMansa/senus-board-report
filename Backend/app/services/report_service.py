import json
import os

from app.models.report import Report
from app.ingestion.downloader import download_report
from app.repositories.report_repository import ReportRepository

CONFIG_PATH = "app/config/report_sources.json"


class ReportService:

    @staticmethod
    def import_reports(db):

        with open(CONFIG_PATH, "r") as file:
            reports = json.load(file)

        imported_reports = []

        for item in reports:

            filename, save_path = download_report(item["url"])

            report = Report(
                title=item["title"],
                company_name=item["company_name"],
                report_type=item["report_type"],
                financial_year=item["financial_year"],
                source_url=item["url"],
                file_name=filename,
                local_path=save_path,
                status="Downloaded"
            )

            report = ReportRepository.create(
                db,
                report,
            )

            imported_reports.append(report)

        return imported_reports

    @staticmethod
    def get_all(db):
        return ReportRepository.get_all(db)

    @staticmethod
    def get_by_id(db, report_id):

        report = ReportRepository.get_by_id(
            db,
            report_id,
        )

        if report is None:
            raise ValueError("Report not found")

        return report

    @staticmethod
    def delete(db, report_id):

        report = ReportRepository.get_by_id(
            db,
            report_id,
        )

        if report is None:
            raise ValueError("Report not found")

        ReportRepository.delete(
            db,
            report,
        )
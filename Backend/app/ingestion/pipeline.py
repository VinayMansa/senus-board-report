from app.ingestion.page_locator import PageLocator
from app.ingestion.metric_extractor import MetricExtractor


class ReportPipeline:

    @staticmethod
    def process(pdf_path: str):

        pages = PageLocator.locate_financial_pages(pdf_path)

        print("Financial Pages:", pages)

        metrics = MetricExtractor.extract_metrics(
            pdf_path,
            pages,
        )

        return metrics
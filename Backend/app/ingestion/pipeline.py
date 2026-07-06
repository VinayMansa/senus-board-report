from app.ingestion.table_extractor import TableExtractor
from app.ingestion.metric_extractor import MetricExtractor


class ReportPipeline:

    @staticmethod
    def process(pdf_path: str):

        tables = TableExtractor.extract_tables(pdf_path)

        metrics = MetricExtractor.extract_metrics(tables)

        return metrics
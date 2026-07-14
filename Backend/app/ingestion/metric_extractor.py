import re
from typing import cast

import fitz


class MetricExtractor:

    PATTERNS = {
        "Turnover": r"Turnover\s*([\(\)\d,]+)",
        "Gross Profit": r"Gross Profit\s*([\(\)\d,]+)",
        "Operating Profit": r"Operating Profit\s*/?\s*\(Loss\)\s*([\(\)\d,]+)",
        "Profit Before Tax": r"Profit\s*/?\s*\(Loss\)\s*Before Tax\s*([\(\)\d,]+)",
        "Profit After Tax": r"Profit\s*/?\s*\(Loss\)\s*After Tax\s*([\(\)\d,]+)",
        "Net Assets": r"Net\s*\(Liabilities\)\s*/\s*Assets\s*([\(\)\d,]+)",
        "Retained Earnings": r"Retained Earnings\s*([\(\)\d,]+)",
    }

    @staticmethod
    def clean_number(value):

        if value is None:
            return None

        value = value.replace(",", "")

        if "(" in value:
            value = "-" + value.replace("(", "").replace(")", "")

        return float(value)

    @classmethod
    def extract_metrics(cls, pdf_path, pages):

        document = fitz.open(pdf_path)

        metrics = []

        for page_number in pages:

            page = document.load_page(page_number - 1)

            text = cast(str, page.get_text("text"))

            for metric, pattern in cls.PATTERNS.items():

                match = re.search(pattern, text, re.MULTILINE)

                if match:

                    metrics.append(
                        {
                            "metric_name": metric,
                            "metric_value": cls.clean_number(
                                match.group(1)
                            ),
                            "unit": "EUR",
                            "page_number": page_number,
                        }
                    )

        document.close()

        return metrics
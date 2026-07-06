import re
import pandas as pd


class MetricExtractor:

    # Keywords we want to detect
    METRICS = [
        "Revenue",
        "Gross Profit",
        "Operating Profit",
        "EBITDA",
        "EBIT",
        "Net Profit",
        "Profit Before Tax",
        "Cash",
        "Cash and Cash Equivalents",
        "Net Debt",
        "Assets",
        "Liabilities",
        "Equity",
        "Customers",
        "ARR",
    ]

    @staticmethod
    def _extract_number(value):

        if value is None:
            return None

        value = str(value)

        # Remove commas and euro symbol
        value = value.replace(",", "")
        value = value.replace("€", "")
        value = value.strip()

        match = re.search(r"-?\d+(\.\d+)?", value)

        if match:
            return float(match.group())

        return None

    @classmethod
    def extract_metrics(cls, tables):

        metrics = []

        for table_data in tables:

            page = table_data["page"]

            df = table_data["table"]

            for _, row in df.iterrows():

                row_values = [
                    str(cell).strip()
                    for cell in row
                    if cell is not None
                ]

                if len(row_values) < 2:
                    continue

                metric_name = row_values[0]

                if metric_name in cls.METRICS:

                    value = None

                    for cell in row_values[1:]:

                        value = cls._extract_number(cell)

                        if value is not None:
                            break

                    if value is not None:

                        metrics.append(
                            {
                                "metric_name": metric_name,
                                "metric_value": value,
                                "unit": "EUR",
                                "page_number": page,
                            }
                        )

        return metrics
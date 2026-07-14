import os
import pdfplumber
import pandas as pd


class TableExtractor:

    @staticmethod
    def extract_tables(pdf_path: str, financial_pages: list[int] | None = None):

        extracted_tables = []

        os.makedirs("debug_tables", exist_ok=True)

        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                if financial_pages is not None and page_number not in financial_pages:
                    continue

                tables = page.extract_tables()

                if not tables:
                    continue

                for index, table in enumerate(tables):

                    if not table:
                        continue

                    df = pd.DataFrame(table)

                    df.to_csv(
                        f"debug_tables/page_{page_number}_{index}.csv",
                        index=False,
                    )

                    extracted_tables.append(
                        {
                            "page": page_number,
                            "table": df,
                        }
                    )

        return extracted_tables

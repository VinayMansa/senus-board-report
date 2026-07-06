import pdfplumber
import pandas as pd


class TableExtractor:

    @staticmethod
    def extract_tables(pdf_path: str):

        extracted_tables = []

        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                tables = page.extract_tables()

                if not tables:
                    continue

                for table in tables:

                    if not table:
                        continue

                    df = pd.DataFrame(table)

                    extracted_tables.append(
                        {
                            "page": page_number,
                            "table": df
                        }
                    )

        return extracted_tables
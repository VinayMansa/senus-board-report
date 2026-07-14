from typing import cast

import fitz


class PageLocator:

    FINANCIAL_KEYWORDS = [
    "turnover",
    "gross profit",
    "operating profit",
    "profit before tax",
    "profit after tax",
    "retained earnings",
    "net (liabilities) / assets",
]

    @staticmethod
    def locate_financial_pages(pdf_path: str):

        document = fitz.open(pdf_path)

        financial_pages = []

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            text = cast(str, page.get_text("text"))

            print("=" * 80)
            print(f"PAGE {page_number + 1}")
            print(text[:500])   # Print first 500 characters

            lower_text = text.lower()

            for keyword in PageLocator.FINANCIAL_KEYWORDS:

                if keyword in lower_text:

                    financial_pages.append(page_number + 1)
                    print(f"FOUND KEYWORD: {keyword}")
                    break

        document.close()

        return financial_pages
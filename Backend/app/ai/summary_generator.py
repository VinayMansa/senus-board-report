from app.models.financial_metric import FinancialMetric


class SummaryGenerator:

    @staticmethod
    def generate(metrics):

        values = {}

        for metric in metrics:
            values[metric.metric_name] = metric.metric_value

        summary = []

        if "Turnover" in values:
            summary.append(
                f"Turnover was €{values['Turnover']:,.0f}."
            )

        if "Gross Profit" in values:
            summary.append(
                f"Gross Profit was €{values['Gross Profit']:,.0f}."
            )

        if "Operating Profit" in values:

            if values["Operating Profit"] < 0:
                summary.append(
                    f"Operating Loss was €{abs(values['Operating Profit']):,.0f}."
                )
            else:
                summary.append(
                    f"Operating Profit was €{values['Operating Profit']:,.0f}."
                )

        if "Profit After Tax" in values:

            if values["Profit After Tax"] < 0:
                summary.append(
                    f"The company reported a Net Loss of €{abs(values['Profit After Tax']):,.0f}."
                )
            else:
                summary.append(
                    f"The company reported a Net Profit of €{values['Profit After Tax']:,.0f}."
                )

        if "Net Assets" in values:

            if values["Net Assets"] < 0:
                summary.append(
                    "Net Assets remain negative."
                )
            else:
                summary.append(
                    "Net Assets remain positive."
                )

        summary.append(
            "Overall, management should continue focusing on improving profitability while sustaining revenue growth."
        )

        return "\n".join(summary)
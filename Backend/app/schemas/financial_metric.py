from pydantic import BaseModel


class FinancialMetricCreate(BaseModel):

    report_id: int

    metric_name: str

    metric_value: float

    unit: str | None = None

    page_number: int | None = None


class FinancialMetricResponse(BaseModel):

    id: int

    report_id: int

    metric_name: str

    metric_value: float

    unit: str | None

    page_number: int | None

    model_config = {
        "from_attributes": True
    }
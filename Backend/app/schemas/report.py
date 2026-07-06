from datetime import datetime

from pydantic import BaseModel, HttpUrl


class ReportCreate(BaseModel):
    title: str
    company_name: str
    report_type: str
    financial_year: int
    source_url: HttpUrl


class ReportResponse(BaseModel):
    id: int
    title: str
    company_name: str
    report_type: str
    financial_year: int
    source_url: str
    file_name: str | None = None
    local_path: str | None = None
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
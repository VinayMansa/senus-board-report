from fastapi import FastAPI
from sqlalchemy import text

from app.database.db import engine  # pyright: ignore[reportMissingImports]
from app.api.user_router import router as user_router
from app.api.report_router import router as report_router
from app.api.financial_metric_router import router as financial_metric_router
from app.api.dashboard_router import router as dashboard_router

app = FastAPI(title="Senus Board Report API")
app.include_router(user_router)
app.include_router(report_router)
app.include_router(financial_metric_router)
app.include_router(dashboard_router)
@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health/db")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "success",
            "database": "Connected"
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }

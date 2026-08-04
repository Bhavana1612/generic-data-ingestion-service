from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import IngestedData
from app.schemas import EndpointRequest
from app.services.ingestion_service import ingest_external_data


router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)


@router.post("/")
def ingest_data(
    request: EndpointRequest,
    db: Session = Depends(get_db)
):

    saved_records = ingest_external_data(
        request.endpoints,
        db
    )

    return {
        "message": "All API data ingested successfully",
        "saved_records": saved_records
    }


@router.get("/")
def get_data(
    db: Session = Depends(get_db)
):

    records = db.query(IngestedData).all()

    return records
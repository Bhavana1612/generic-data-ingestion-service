from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import IngestedData
from app.schemas import EndpointRequest
import requests


router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)


@router.post("/")
def ingest_data(request: EndpointRequest, db: Session = Depends(get_db)):

    saved_records = []

    for endpoint in request.endpoints:

        try:
            response = requests.get(endpoint)
            response.raise_for_status()

            api_data = response.json()

        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to fetch {endpoint}: {str(e)}"
            )

        record = IngestedData(
            name="External API",
            data=api_data
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        saved_records.append(record.id)

    return {
        "message": "All API data ingested successfully",
        "saved_records": saved_records
    }


@router.get("/")
def get_data(db: Session = Depends(get_db)):

    records = db.query(IngestedData).all()

    return records
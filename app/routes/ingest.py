from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import IngestedData


router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)


@router.post("/")
def ingest_data(data: dict, db: Session = Depends(get_db)):

    record = IngestedData(
        name=data.get("name"),
        data=data
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "message": "Data ingestion successful",
        "id": record.id,
        "received_data": data
    }


@router.get("/")
def get_data(db: Session = Depends(get_db)):

    records = db.query(IngestedData).all()

    return records
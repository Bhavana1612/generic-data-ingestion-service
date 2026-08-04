import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import IngestedData


def ingest_external_data(endpoints, db: Session):

    saved_records = []

    for endpoint in endpoints:

        try:
            response = requests.get(
                endpoint,
                timeout=10
            )

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

    return saved_records
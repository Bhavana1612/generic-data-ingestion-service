import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import IngestedData


def ingest_external_data(sources, db: Session):

    saved_records = []

    for source in sources:

        endpoint = source.url
        headers = source.headers

        try:
            response = requests.get(
                endpoint,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            api_data = response.json()

        except requests.exceptions.Timeout:
            raise HTTPException(
                status_code=408,
                detail=f"Request timeout for {endpoint}"
            )

        except requests.exceptions.HTTPError:
            raise HTTPException(
                status_code=400,
                detail=f"API returned an error for {endpoint}"
            )

        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=400,
                detail=f"Unable to connect to external API: {endpoint}"
            )

        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid JSON response from {endpoint}"
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
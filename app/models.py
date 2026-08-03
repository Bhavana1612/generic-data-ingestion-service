from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class IngestedData(Base):
    __tablename__ = "ingested_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    data = Column(JSON)
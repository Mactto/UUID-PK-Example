from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class TextPkTable(Base):
    __tablename__ = "text_pk_table"
    pk = Column(String, primary_key=True, index=True)

class UUIDPkTable(Base):
    __tablename__ = "uuid_pk_table"
    pk = Column(UUID, primary_key=True, index=True)
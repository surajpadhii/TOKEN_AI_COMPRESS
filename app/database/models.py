from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from app.database.database import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    api_key = Column(String, unique=True, nullable=False)
    plan = Column(String, default="Free")
    active = Column(Boolean, default=True)


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True)

    client_id = Column(Integer, ForeignKey("api_keys.id"))

    original_tokens = Column(Integer)
    compressed_tokens = Column(Integer)
    tokens_saved = Column(Integer)

    compression_ratio = Column(Float)
    processing_time_ms = Column(Float)

    compression_mode = Column(String)

    caveman_enabled = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
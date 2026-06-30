from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import UsageLog
from datetime import datetime, timedelta
from datetime import datetime, timedelta
class UsageService:
    """
    Service responsible for saving and retrieving usage logs.
    """

    def create_log(
        self,
        db: Session,
        client_id: int,
        original_tokens: int,
        compressed_tokens: int,
        tokens_saved: int,
        compression_ratio: float,
        processing_time_ms: float,
        compression_mode: str,
        caveman_enabled: bool,
    ):
        usage = UsageLog(
            client_id=client_id,
            original_tokens=original_tokens,
            compressed_tokens=compressed_tokens,
            tokens_saved=tokens_saved,
            compression_ratio=compression_ratio,
            processing_time_ms=processing_time_ms,
            compression_mode=compression_mode,
            caveman_enabled=caveman_enabled,
        )
        def requests_last_minute(
            self,
            db: Session,
            client_id: int,
):
         one_minute_ago = datetime.utcnow() - timedelta(minutes=1)

         return (
        db.query(func.count(UsageLog.id))
        .filter(
            UsageLog.client_id == client_id,
            UsageLog.created_at >= one_minute_ago,
        )
        .scalar()
        or 0
    )
        db.add(usage)
        db.commit()
        db.refresh(usage)

        return usage

    def today_requests(
        self,
        db: Session,
        client_id: int,
    ):
        return (
            db.query(func.count(UsageLog.id))
            .filter(
                UsageLog.client_id == client_id,
                func.date(UsageLog.created_at) == date.today(),
            )
            .scalar()
        )
    def last_minute_requests(
    self,
    db: Session,
    client_id: int,
    ):
        one_minute_ago = datetime.utcnow() - timedelta(minutes=1)

        return (
        db.query(func.count(UsageLog.id))
        .filter(
            UsageLog.client_id == client_id,
            UsageLog.created_at >= one_minute_ago,
        )
        .scalar()
    )


usage_service = UsageService()
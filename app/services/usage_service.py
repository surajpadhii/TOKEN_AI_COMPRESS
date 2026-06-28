from sqlalchemy.orm import Session

from app.database.models import UsageLog


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

        db.add(usage)
        db.commit()
        db.refresh(usage)

        return usage


usage_service = UsageService()
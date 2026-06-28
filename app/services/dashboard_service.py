from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import UsageLog


class DashboardService:

    def get_summary(self, db: Session):
        ...
        return {...}

    def get_history(
        self,
        db: Session,
    ):
        logs = (
            db.query(UsageLog)
            .order_by(UsageLog.created_at.desc())
            .all()
        )

        return [
            {
                "id": log.id,
                "client_id": log.client_id,
                "original_tokens": log.original_tokens,
                "compressed_tokens": log.compressed_tokens,
                "tokens_saved": log.tokens_saved,
                "compression_ratio": log.compression_ratio,
                "processing_time_ms": log.processing_time_ms,
                "compression_mode": log.compression_mode,
                "caveman_enabled": log.caveman_enabled,
                "created_at": log.created_at,
            }
            for log in logs
        ]

    def get_client_summary(
        self,
        db: Session,
        client_id: int,
    ):
        total_requests = (
            db.query(UsageLog)
            .filter(UsageLog.client_id == client_id)
            .count()
        )

        original_tokens = (
            db.query(func.sum(UsageLog.original_tokens))
            .filter(UsageLog.client_id == client_id)
            .scalar() or 0
        )

        compressed_tokens = (
            db.query(func.sum(UsageLog.compressed_tokens))
            .filter(UsageLog.client_id == client_id)
            .scalar() or 0
        )

        tokens_saved = (
            db.query(func.sum(UsageLog.tokens_saved))
            .filter(UsageLog.client_id == client_id)
            .scalar() or 0
        )

        avg_ratio = (
            db.query(func.avg(UsageLog.compression_ratio))
            .filter(UsageLog.client_id == client_id)
            .scalar() or 0
        )

        avg_time = (
            db.query(func.avg(UsageLog.processing_time_ms))
            .filter(UsageLog.client_id == client_id)
            .scalar() or 0
        )

        return {
            "client_id": client_id,
            "total_requests": total_requests,
            "original_tokens": original_tokens,
            "compressed_tokens": compressed_tokens,
            "tokens_saved": tokens_saved,
            "average_ratio": round(avg_ratio, 3),
            "average_processing_time_ms": round(avg_time, 2),
        }


dashboard_service = DashboardService()
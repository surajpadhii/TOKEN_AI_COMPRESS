import time

from sqlalchemy.orm import Session

from app.ai.headroom_client import headroom_client
from app.core.compression_modes import COMPRESSION_MODES
from app.core.enums import CompressionMode
from app.core.logger import logger
from app.database.models import APIKey
from app.services.usage_service import usage_service
from app.services.plan_service import plan_service
from app.core.request_id import generate_request_id

class CompressionService:
    """
    Business logic for document compression.
    """

    def compress(
        self,
        db: Session,
        client: APIKey,
        content: str,
        content_type: str = "markdown",
        compression_mode: CompressionMode = CompressionMode.balanced,
        use_caveman: bool = False,
    ):
        start = time.perf_counter()
        request_id = generate_request_id()
        plan_service.validate_mode(
        client,
        compression_mode,
        )
        plan_service.validate_daily_limit(
        db,
        client,
        )
        plan_service.validate_rate_limit(
        db,
        client,
    )
        target_ratio = COMPRESSION_MODES[compression_mode.value]

        try:
            result = headroom_client.compress(
                content=content,
                content_type=content_type,
                target_ratio=target_ratio,
            )

            elapsed_ms = round(
                (time.perf_counter() - start) * 1000,
                2,
            )

            logger.info(
                f"[{request_id}] "
                f"Compression completed | "
                f"Mode={compression_mode.value} | "
                f"Original={result.original_tokens}, "
                f"Compressed={result.compressed_tokens}, "
                f"Saved={result.tokens_saved}, "
                f"Ratio={result.compression_ratio:.2f}, "
                f"Time={elapsed_ms} ms"
            )

            usage_service.create_log(
                db=db,
                client_id=client.id,
                original_tokens=result.original_tokens,
                compressed_tokens=result.compressed_tokens,
                tokens_saved=result.tokens_saved,
                compression_ratio=result.compression_ratio,
                processing_time_ms=elapsed_ms,
                compression_mode=compression_mode.value,
                caveman_enabled=use_caveman,
            )

            return {
                "request_id": request_id,
                "compressed": result.compressed,
                "original": result.original,
                "original_tokens": result.original_tokens,
                "compressed_tokens": result.compressed_tokens,
                "tokens_saved": result.tokens_saved,
                "savings_percentage": result.savings_percentage,
                "compression_ratio": result.compression_ratio,
                "model_used": result.model_used,
                "processing_time_ms": elapsed_ms,
                "compression_mode": compression_mode.value,
                "caveman_enabled": use_caveman,
            }

        except Exception:
            logger.exception("Compression failed")
            raise


compression_service = CompressionService()
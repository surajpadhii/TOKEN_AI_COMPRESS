from pydantic import BaseModel


class CompressionResponse(BaseModel):
    request_id: str
    compressed: str
    original: str
    original_tokens: int
    compressed_tokens: int
    tokens_saved: int
    savings_percentage: float
    compression_ratio: float
    model_used: str
    processing_time_ms: float
    compression_mode: str
    caveman_enabled: bool
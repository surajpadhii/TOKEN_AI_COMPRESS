from pydantic import BaseModel

from app.core.enums import CompressionMode


class CompressionRequest(BaseModel):
    content: str
    content_type: str = "markdown"

    compression_mode: CompressionMode = CompressionMode.balanced

    use_caveman: bool = False
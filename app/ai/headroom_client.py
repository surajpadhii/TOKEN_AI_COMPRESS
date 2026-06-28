from headroom.transforms.kompress_compressor import (
    KompressCompressor,
    KompressConfig,
)


class HeadroomClient:
    """
    Singleton wrapper around KompressCompressor.
    The model is loaded once and reused for every request.
    """

    def __init__(self):
        self.compressor = KompressCompressor(
            KompressConfig()
        )

    def preload(self):
        """Load the model into memory."""
        self.compressor.preload()

    def compress(
        self,
        content: str,
        content_type: str = "markdown",
        target_ratio: float = 0.5,
    ):
        return self.compressor.compress(
            content=content,
            content_type=content_type,
            target_ratio=target_ratio,
        )


# Global singleton instance
headroom_client = HeadroomClient()

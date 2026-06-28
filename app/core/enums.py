from enum import Enum


class CompressionMode(str, Enum):
    fast = "fast"
    balanced = "balanced"
    maximum = "maximum"
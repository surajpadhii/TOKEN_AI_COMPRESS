from loguru import logger
import sys

# Remove Loguru's default logger
logger.remove()

# Log to the terminal
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)

# Log to a file
logger.add(
    "logs/headroom.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)
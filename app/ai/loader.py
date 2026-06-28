from transformers import AutoTokenizer

from app.ai.device import get_device
from app.core.config import settings


class ModelLoader:
    def __init__(self):
        self.device = get_device()

        print(f"Loading on {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.MODEL_NAME
        )

        print("Tokenizer Loaded")


loader = ModelLoader()
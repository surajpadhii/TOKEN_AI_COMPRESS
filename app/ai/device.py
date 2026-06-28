import torch


def get_device() -> str:
    """
    Return the best available device.
    Priority:
        1. Apple Silicon (MPS)
        2. CUDA
        3. CPU
    """
    if torch.backends.mps.is_available():
        return "mps"

    if torch.cuda.is_available():
        return "cuda"

    return "cpu"

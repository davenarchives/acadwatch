from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Runtime configuration for the dropout prediction app."""

    MODEL_PATH = BASE_DIR / "dropout_model.pkl"

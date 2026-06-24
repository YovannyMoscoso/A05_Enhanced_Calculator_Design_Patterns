"""Configuration management for the calculator application."""

import os

from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Loads calculator configuration from environment variables."""

    def __init__(self) -> None:
        load_dotenv()

        self.history_file = os.getenv("HISTORY_FILE", "history.csv")
        self.max_history_size = int(os.getenv("MAX_HISTORY_SIZE", "100"))
        self.auto_save = os.getenv("AUTO_SAVE", "true").lower() == "true"

        self.validate()

    def validate(self) -> None:
        if self.max_history_size <= 0:
            raise ConfigurationError("MAX_HISTORY_SIZE must be greater than zero.")

    @property
    def history_path(self) -> str:
        return self.history_file
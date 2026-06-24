"""Calculation model for the enhanced calculator application."""

from dataclasses import dataclass
from datetime import datetime

from app.operations import OperationFactory


@dataclass
class Calculation:
    """Represents one calculator operation."""

    operation: str
    a: float
    b: float
    result: float | None = None
    timestamp: str | None = None

    def __post_init__(self) -> None:
        if self.result is None:
            operation_obj = OperationFactory.create_operation(self.operation)
            self.result = operation_obj.execute(self.a, self.b)

        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat(timespec="seconds")

    def to_dict(self) -> dict:
        """Serialize calculation to a dictionary."""
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Calculation":
        """Deserialize calculation from a dictionary."""
        return cls(
            operation=data["operation"],
            a=float(data["a"]),
            b=float(data["b"]),
            result=float(data["result"]),
            timestamp=data["timestamp"],
        )
"""Arithmetic operations and factory pattern implementation."""

from abc import ABC, abstractmethod

from app.exceptions import OperationError


class Operation(ABC):
    """Abstract base class for all operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        return a ** (1 / b)


class OperationFactory:
    """Factory class for creating operations."""

    @staticmethod
    def create_operation(operation_name: str) -> Operation:

        operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "root": Root(),
        }

        if operation_name.lower() not in operations:
            raise OperationError(f"Unsupported operation: {operation_name}")

        return operations[operation_name.lower()]
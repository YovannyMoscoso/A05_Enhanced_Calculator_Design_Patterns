"""Input validation for the calculator application."""

from app.exceptions import ValidationError


class InputValidator:
    """Validates user input for calculator operations."""

    VALID_OPERATIONS = {"add", "subtract", "multiply", "divide", "power", "root"}
    VALID_COMMANDS = {
        "help",
        "history",
        "clear",
        "undo",
        "redo",
        "save",
        "load",
        "exit",
    }

    @classmethod
    def validate_operation(cls, operation: str) -> str:
        operation = operation.lower().strip()

        if operation not in cls.VALID_OPERATIONS:
            raise ValidationError(f"Invalid operation: {operation}")

        return operation

    @classmethod
    def is_command(cls, user_input: str) -> bool:
        return user_input.lower().strip() in cls.VALID_COMMANDS

    @staticmethod
    def validate_number(value: str) -> float:
        try:
            return float(value)
        except ValueError as error:
            raise ValidationError(f"Invalid number: {value}") from error
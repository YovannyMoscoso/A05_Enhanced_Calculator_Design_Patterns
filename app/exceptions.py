"""Custom exceptions for the enhanced calculator application."""


class CalculatorError(Exception):
    """Base exception for calculator-related errors."""


class ValidationError(CalculatorError):
    """Raised when user input is invalid."""


class OperationError(CalculatorError):
    """Raised when an arithmetic operation cannot be completed."""


class ConfigurationError(CalculatorError):
    """Raised when application configuration is invalid."""


class HistoryError(CalculatorError):
    """Raised when history data cannot be saved, loaded, or managed."""
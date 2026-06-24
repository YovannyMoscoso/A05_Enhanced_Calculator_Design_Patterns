"""Memento pattern implementation for calculator state."""


class CalculatorMemento:
    """Stores a snapshot of calculator history."""

    def __init__(self, history):
        self._history = history.copy()

    def get_state(self):
        """Return saved state."""
        return self._history.copy()
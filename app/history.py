"""History management and observer pattern implementation."""

from abc import ABC, abstractmethod

import pandas as pd

from app.calculation import Calculation
from app.exceptions import HistoryError


class HistoryObserver(ABC):
    """Abstract observer for history updates."""

    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        pass


class LoggingObserver(HistoryObserver):
    """Observer that logs new calculations to the console."""

    def update(self, calculation: Calculation) -> None:
        print(f"New calculation: {calculation.operation} = {calculation.result}")


class AutoSaveObserver(HistoryObserver):
    """Observer that automatically saves history when updated."""

    def __init__(self, history_manager: "HistoryManager") -> None:
        self.history_manager = history_manager

    def update(self, calculation: Calculation) -> None:
        self.history_manager.save_history()


class HistoryManager:
    """Manages calculation history using pandas."""

    def __init__(self, file_path: str = "history.csv", max_size: int = 100) -> None:
        self.file_path = file_path
        self.max_size = max_size
        self.calculations: list[Calculation] = []
        self.observers: list[HistoryObserver] = []

    def add_observer(self, observer: HistoryObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self, calculation: Calculation) -> None:
        for observer in self.observers:
            observer.update(calculation)

    def add_calculation(self, calculation: Calculation) -> None:
        self.calculations.append(calculation)

        if len(self.calculations) > self.max_size:
            self.calculations.pop(0)

        self.notify_observers(calculation)

    def clear_history(self) -> None:
        self.calculations.clear()

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([calculation.to_dict() for calculation in self.calculations])

    def save_history(self) -> None:
        try:
            self.to_dataframe().to_csv(self.file_path, index=False)
        except Exception as error:
            raise HistoryError(f"Could not save history: {error}") from error

    def load_history(self) -> None:
        try:
            dataframe = pd.read_csv(self.file_path)
            self.calculations = [
                Calculation.from_dict(row.to_dict())
                for _, row in dataframe.iterrows()
            ]
        except FileNotFoundError:
            self.calculations = []
        except Exception as error:
            raise HistoryError(f"Could not load history: {error}") from error
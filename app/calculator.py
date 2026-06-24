"""Main calculator facade and REPL interface."""

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.exceptions import CalculatorError, ValidationError
from app.history import AutoSaveObserver, HistoryManager, LoggingObserver
from app.input_validators import InputValidator


class Calculator:
    """Facade class that connects operations, history, config, and REPL."""

    def __init__(self) -> None:
        self.config = CalculatorConfig()
        self.history = HistoryManager(
            file_path=self.config.history_path,
            max_size=self.config.max_history_size,
        )
        self.undo_stack: list[CalculatorMemento] = []
        self.redo_stack: list[CalculatorMemento] = []

        self.history.add_observer(LoggingObserver())

        if self.config.auto_save:
            self.history.add_observer(AutoSaveObserver(self.history))

    def save_state(self) -> None:
        self.undo_stack.append(CalculatorMemento(self.history.calculations))
        self.redo_stack.clear()

    def perform_calculation(self, operation: str, a: float, b: float) -> Calculation:
        operation = InputValidator.validate_operation(operation)
        self.save_state()

        calculation = Calculation(operation=operation, a=a, b=b)
        self.history.add_calculation(calculation)

        return calculation

    def undo(self) -> str:
        if not self.undo_stack:
            return "Nothing to undo."

        self.redo_stack.append(CalculatorMemento(self.history.calculations))
        previous_state = self.undo_stack.pop()
        self.history.calculations = previous_state.get_state()

        return "Undo completed."

    def redo(self) -> str:
        if not self.redo_stack:
            return "Nothing to redo."

        self.undo_stack.append(CalculatorMemento(self.history.calculations))
        next_state = self.redo_stack.pop()
        self.history.calculations = next_state.get_state()

        return "Redo completed."

    def show_history(self) -> str:
        if not self.history.calculations:
            return "History is empty."

        lines = []
        for index, calculation in enumerate(self.history.calculations, start=1):
            lines.append(
                f"{index}. {calculation.a} {calculation.operation} "
                f"{calculation.b} = {calculation.result}"
            )

        return "\n".join(lines)

    def clear_history(self) -> str:
        self.save_state()
        self.history.clear_history()
        return "History cleared."

    def save_history(self) -> str:
        self.history.save_history()
        return "History saved."

    def load_history(self) -> str:
        self.save_state()
        self.history.load_history()
        return "History loaded."

    def help_text(self) -> str:
        return (
            "Available operations: add, subtract, multiply, divide, power, root\n"
            "Available commands: help, history, clear, undo, redo, save, load, exit"
        )

    def handle_command(self, command: str) -> str:
        command = command.lower().strip()

        if command == "help":
            return self.help_text()
        if command == "history":
            return self.show_history()
        if command == "clear":
            return self.clear_history()
        if command == "undo":
            return self.undo()
        if command == "redo":
            return self.redo()
        if command == "save":
            return self.save_history()
        if command == "load":
            return self.load_history()
        if command == "exit":
            return "Goodbye!"

        raise ValidationError(f"Unknown command: {command}")

    def run(self) -> None:
        print("Enhanced Calculator Application")
        print(self.help_text())

        while True:
            user_input = input("\nEnter operation or command: ").strip()

            try:
                if InputValidator.is_command(user_input):
                    message = self.handle_command(user_input)
                    print(message)

                    if user_input.lower() == "exit":
                        break

                    continue

                operation = InputValidator.validate_operation(user_input)
                first_number = InputValidator.validate_number(input("Enter first number: "))
                second_number = InputValidator.validate_number(input("Enter second number: "))

                calculation = self.perform_calculation(
                    operation,
                    first_number,
                    second_number,
                )

                print(f"Result: {calculation.result}")

            except CalculatorError as error:
                print(f"Error: {error}")
            except Exception as error:
                print(f"Unexpected error: {error}")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
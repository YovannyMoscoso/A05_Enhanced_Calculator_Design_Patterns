from app.calculator import Calculator


def test_perform_calculation():
    calculator = Calculator()

    calc = calculator.perform_calculation("add", 5, 3)

    assert calc.result == 8
    assert len(calculator.history.calculations) == 1


def test_show_history():
    calculator = Calculator()
    calculator.perform_calculation("add", 5, 3)

    output = calculator.show_history()

    assert "5" in output
    assert "add" in output
    assert "8" in output


def test_undo_redo():
    calculator = Calculator()
    calculator.perform_calculation("add", 5, 3)

    undo_message = calculator.undo()
    assert undo_message == "Undo completed."
    assert len(calculator.history.calculations) == 0

    redo_message = calculator.redo()
    assert redo_message == "Redo completed."
    assert len(calculator.history.calculations) == 1


def test_clear_history():
    calculator = Calculator()
    calculator.perform_calculation("add", 5, 3)

    message = calculator.clear_history()

    assert message == "History cleared."
    assert len(calculator.history.calculations) == 0


def test_help_text():
    calculator = Calculator()

    output = calculator.help_text()

    assert "Available operations" in output
    assert "Available commands" in output
from app.calculation import Calculation


def test_calculation_add():
    calc = Calculation(operation="add", a=5, b=3)

    assert calc.operation == "add"
    assert calc.a == 5
    assert calc.b == 3
    assert calc.result == 8


def test_calculation_to_dict():
    calc = Calculation(operation="multiply", a=4, b=2)
    data = calc.to_dict()

    assert data["operation"] == "multiply"
    assert data["a"] == 4
    assert data["b"] == 2
    assert data["result"] == 8
    assert "timestamp" in data


def test_calculation_from_dict():
    data = {
        "operation": "subtract",
        "a": 10,
        "b": 4,
        "result": 6,
        "timestamp": "2026-01-01T10:00:00",
    }

    calc = Calculation.from_dict(data)

    assert calc.operation == "subtract"
    assert calc.a == 10
    assert calc.b == 4
    assert calc.result == 6
    assert calc.timestamp == "2026-01-01T10:00:00"
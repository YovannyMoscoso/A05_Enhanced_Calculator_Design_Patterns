from app.calculation import Calculation
from app.history import HistoryManager


def test_add_calculation():
    history = HistoryManager()
    calc = Calculation(operation="add", a=5, b=3)

    history.add_calculation(calc)

    assert len(history.calculations) == 1
    assert history.calculations[0].result == 8


def test_clear_history():
    history = HistoryManager()
    history.add_calculation(Calculation(operation="add", a=5, b=3))

    history.clear_history()

    assert history.calculations == []


def test_to_dataframe():
    history = HistoryManager()
    history.add_calculation(Calculation(operation="multiply", a=4, b=2))

    df = history.to_dataframe()

    assert len(df) == 1
    assert df.iloc[0]["operation"] == "multiply"
    assert df.iloc[0]["result"] == 8
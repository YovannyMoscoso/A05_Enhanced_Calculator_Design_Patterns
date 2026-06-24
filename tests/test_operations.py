import pytest

from app.exceptions import OperationError
from app.operations import Add, Divide, Multiply, OperationFactory, Power, Root, Subtract


def test_add():
    assert Add().execute(5, 3) == 8


def test_subtract():
    assert Subtract().execute(5, 3) == 2


def test_multiply():
    assert Multiply().execute(5, 3) == 15


def test_divide():
    assert Divide().execute(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(OperationError):
        Divide().execute(5, 0)


def test_power():
    assert Power().execute(2, 3) == 8


def test_root():
    assert Root().execute(9, 2) == 3


def test_root_degree_zero():
    with pytest.raises(OperationError):
        Root().execute(9, 0)


def test_operation_factory():
    operation = OperationFactory.create_operation("add")
    assert isinstance(operation, Add)


def test_operation_factory_invalid():
    with pytest.raises(OperationError):
        OperationFactory.create_operation("invalid")
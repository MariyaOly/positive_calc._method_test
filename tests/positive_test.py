import pytest

from app.calc import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 2)
    assert result == 3

def test_multiply():
    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20

def test_divide():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5

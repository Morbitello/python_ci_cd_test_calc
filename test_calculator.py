# test_calculator.py
import pytest
from calculator import Calculator

# Create an instance of the Calculator class
calc = Calculator()

def test_add():
    assert calc.add(1, 2) == 3

def test_subtract():
    assert calc.subtract(5, 3) == 2

def test_multiply():
    assert calc.multiply(2, 3) == 6

def test_divide():
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(1, 0)

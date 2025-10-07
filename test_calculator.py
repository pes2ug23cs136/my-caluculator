import pytest 
from src.calculator import add,subtract

class TestBasicOperations:
    def test_add_positive_number(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    def test_substract_postive_number(self):
        assert substract(5, 3) == 2
        assert substract(10, 4) == 6
    def test_add_negative_numbers(self):

        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
    def test_subtract_negative_numbers(self):

        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2
import pytest
from src.calculator import Calculator  # 从src导入

class TestCalculator:
    def test_add(self):
        assert Calculator.add(2, 3) == 5

    def test_divide(self):
        assert Calculator.divide(6, 3) == 2.0
        with pytest.raises(ValueError):
            Calculator.divide(1, 0)
from typing import Union

Number = Union[int, float]


class Operations:
    """Provides basic arithmetic operations."""

    @staticmethod
    def addition(a: Number, b: Number) -> Number:
        return a + b

    @staticmethod
    def subtraction(a: Number, b: Number) -> Number:
        return a - b

    @staticmethod
    def multiplication(a: Number, b: Number) -> Number:
        return a * b

    @staticmethod
    def division(a: Number, b: Number) -> Number:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
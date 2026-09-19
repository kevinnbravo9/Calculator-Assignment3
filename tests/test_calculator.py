from unittest.mock import patch
from app.calculator import calculator

def test_calculator_addition(capsys):
    with patch('builtins.input', side_effect=['2 + 3', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_calculator_subtraction(capsys):
    with patch('builtins.input', side_effect=['5 - 2', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Result: 3.0" in captured.out

def test_calculator_multiplication(capsys):
    with patch('builtins.input', side_effect=['2 * 3', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

def test_calculator_division(capsys):
    with patch('builtins.input', side_effect=['6 / 2', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Result: 3.0" in captured.out

def test_calculator_invalid_input(capsys):
    with patch('builtins.input', side_effect=['invalid input', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Error: Invalid input format. Use: number operator number" in captured.out

def test_calculator_division_by_zero(capsys):
    with patch('builtins.input', side_effect=['5 / 0', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out

def test_calculator_exit(capsys):
    with patch('builtins.input', side_effect=['exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Exiting the calculator. Goodbye!" in captured.out

def test_calculator_invalid_operator(capsys):
    with patch('builtins.input', side_effect=['2 ^ 3', 'exit']):
        calculator()
    captured = capsys.readouterr()
    assert "Error: Unsupported operator: ^" in captured.out

def test_calculator_unexpected_error(capsys):
    with patch('builtins.input', side_effect=['2 + 3', 'exit']):
        with patch('app.calculator.Operations.addition',
                   side_effect=Exception("Unexpected error")):
            calculator()

    captured = capsys.readouterr()
    assert "An unexpected error occurred: Unexpected error" in captured.out
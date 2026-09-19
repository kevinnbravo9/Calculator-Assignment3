# Module 3 Calculator

This project is a command-line calculator created in Python. The calculator uses a REPL (Read-Eval-Print Loop) that allows the user to enter mathematical operations continuously until they choose to exit.

## Features

The calculator supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division
- Input validation
- Division by zero error handling
- Invalid operator handling
- Unexpected error handling

## How to Run the Calculator

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the calculator:

```bash
python3 main.py
```

Enter an operation using this format:

```text
2 + 2
```

Type `exit` to close the calculator.

## Testing

This project uses pytest for automated testing.

Run the tests with:

```bash
pytest
```

To run the tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

The project includes unit tests, parameterized tests, and tests for the calculator REPL and error handling.

## Continuous Integration

GitHub Actions is configured to automatically run the tests when changes are pushed to the main branch or when a pull request is created.

## Project Structure

The project is organized into different folders and files:

- `app/calculator/` - Contains the calculator REPL.
- `app/operations/` - Contains the math operations.
- `tests/` - Contains the tests for the calculator and operations.
- `main.py` - Runs the calculator.
- `requirements.txt` - Contains the required Python packages.
- `pytest.ini` - Contains the pytest configuration.
- `.coveragerc` - Contains the coverage configuration.
- `.github/workflows/tests.yml` - Runs the tests automatically with GitHub Actions.
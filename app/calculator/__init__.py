from app.operations import Operations

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    print("Welcome to the Basic REPL Calculator!")
    print("Type 'exit' to quit.") 
    while True:
        user_input = input("Enter operation (e.g., 2 + 2): ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Use: number operator number")

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            if operator == '+':
                result = Operations.addition(a, b)
            elif operator == '-':
                result = Operations.subtraction(a, b)
            elif operator == '*':
                result = Operations.multiplication(a, b)
            elif operator == '/':
                result = Operations.division(a, b)
            else:
                raise ValueError(f"Unsupported operator: {operator}")

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
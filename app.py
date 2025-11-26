def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def main():
    print("Basic CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    if choice not in {'1', '2', '3', '4'}:
        print("Invalid choice")
        return

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    try:
        if choice == '1':
            result = add(a, b)
            op = '+'
        elif choice == '2':
            result = subtract(a, b)
            op = '-'
        elif choice == '3':
            result = multiply(a, b)
            op = '*'
        elif choice == '4':
            result = divide(a, b)
            op = '/'
        print(f"{a} {op} {b} = {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

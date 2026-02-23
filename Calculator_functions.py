# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Division by zero."

# displaying operations menu
while True:
    print("\nCalculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    # Taking user input for menu choice
    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Exiting the calculator. Goodbye!")
        break

    # For choices 1-5, take user inputs for two numbers
    a = float(input("Enter first number (A): "))
    b = float(input("Enter second number (B): "))

    # Perform the operation
    if choice == 1:
        print(f"{a} + {b} = {add(a, b)}")
    elif choice == 2:
        print(f"{a} - {b} = {subtract(a, b)}")
    elif choice == 3:
        print(f"{a} * {b} = {multiply(a, b)}")
    elif choice == 4:
        print(f"{a} / {b} = {divide(a, b)}")
    elif choice == 5:
        print(f"{a} % {b} = {modulus(a, b)}")
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")


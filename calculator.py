def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "⚠️ Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "⚠️ Error: Modulus by zero"
    return a % b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def show_menu():
    print("\n=== Simple Calculator ===")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    print("5. % Modulus")
    print("6. ^ Exponentiation")
    print("7. 🚪 Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation (1-7): ").strip()

        if choice == '7':
            print("👋 Exiting calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = None

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = modulus(num1, num2)
        elif choice == '6':
            result = power(num1, num2)
        else:
            print("❌ Invalid choice. Please try again.")
            continue

        print(f"🧮 Result: {result}")

if __name__ == "__main__":
    main()

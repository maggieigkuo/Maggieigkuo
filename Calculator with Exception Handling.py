import logging

#Configure logging for error tracking
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

#Show menu to user
def menu():
    print("🧮 Welcome to the Error-Free Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

#Input validation: ensures a valid float is returned
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

#Division with exception handling and logging
def divide_with_logging(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError occurred: {e}")
        print("⚠️ Oops! Division by zero is not allowed.")
        return None

#Main calculator function
def calculator():
    while True:
        menu()
        choice = input("Enter your choice (1–5): ")

        if choice == '5':
            print("👋 Goodbye!")
            break
        elif choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                if choice == '1':
                    result = num1 + num2
                    print(f"✅ The result is {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"✅ The result is {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"✅ The result is {result}")
                elif choice == '4':
                    result = divide_with_logging(num1, num2)
                    if result is not None:
                        print(f"✅ The result is {result}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print("⚠️ An unexpected error occurred. Please try again.")
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

#Run the calculator
if __name__ == "__main__":
    calculator()
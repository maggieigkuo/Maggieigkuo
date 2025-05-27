#Menu of Recursive Functions
import turtle

#Recursive function to calculate factorial
def factorial(n):
    if n == 1: 
        return 1
    return n * factorial(n-1)

#Recursive function to calculate nth Fibonacci number
def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

#Recursive fractal tree pattern using turtle 
def draw_tree(branch_len):
    if branch_len > 5:
        turtle.forward(branch_len)
        turtle.right(20)
        draw_tree(branch_len - 15)
        turtle.left(40)
        draw_tree(branch_len - 15)
        turtle.right(20)
        turtle.backward(branch_len)

#Fractal tree wrapper to setup turtle screen
def draw_fractal_tree():
    turtle.speed('fastest')
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    draw_tree(75)
    turtle.done()

#Validate positive integer input
def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("❗ Please enter a non-negative integer.")
        except ValueError:
            print("❗ Invalid input. Please enter a valid number.")

# Main menu function
def menu():
    while True:
        print("🌟 Welcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")
        
        if choice == '1':
            num = get_positive_int("Enter a number to find its factorial: ")
            print(f"✅ The factorial of {num} is {factorial(num)}.")
        
        elif choice == '2':
            n = get_positive_int("Enter the position of the Fibonacci number: ")
            print(f"✅ The {n}th Fibonacci number is {fibonacci_sequence(n)}.")
        
        elif choice == '3':
            print("🌲 Drawing fractal tree...")
            draw_fractal_tree()
        
        elif choice == '4':
            print("👋 Goodbye! Thanks for using the Recursive Artistry Program.")
            break
        
        else:
            print("❌ Invalid option. Please choose a number from 1 to 4.")

# Start the program
if __name__ == "__main__":
    menu()

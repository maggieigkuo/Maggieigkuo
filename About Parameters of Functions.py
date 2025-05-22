#Task 1 - Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a,b):
    return a+b

name = input("Enter your name: ")
greet_user(name)

num1 = 21
num2 = 5
result_addition=add_numbers(num1,num2)

print(f"The sum of {num1} and {num2} is", result_addition)

#Task 2 - Using Default Parameters
pet_name = input("Enter your dog's name: ")
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("pet_name")
describe_pet("Melo", "cat")

#Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print(f"Making a sandwhich with the following ingredients:")
    for item in ingredients:
        print(f"{item}")
make_sandwich("Ciabatta", "Turkey", "Tomato", "Pepper Jack")

#Task 4 - Understanding Recursion
n = int(input("Enter a number: "))
def factorial(n):
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1)
result = factorial(n)
print(f"Factorial of {n} is {result}.")

n = int(input("Enter a number: "))
def fibonacci_sequence(n):
    if n < 0:
        print("Incorrect")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
result = fibonacci_sequence(n)
print(f"The {n}th Fibonacci number is {result}.")
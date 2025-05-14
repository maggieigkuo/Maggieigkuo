#Task 1 - Counting Down with Loops
number = int(input("Enter a starting number: "))

while number>0:
    print(number, end=" ")
    number -= 1
print("Blast off! 🚀")

#Task 2 - Multiplication Table with for Loops
number = int(input("Please enter a number for me to multiply 🤓: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}") 

#Task 3 - Find the Factorial
number = int(input("Think of a number 🤔: "))
# Initialize the factorial variable to 1
fact = 1 

# Using a for loop to figure out the factorial
for i in range(1, number+1):
    fact *= i #fact = fact * i
print(f"Did you know the factorial of {number} is {fact}!")
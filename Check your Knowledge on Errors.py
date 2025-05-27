#Task 1 - Understanding Python Exceptions
try:
    number = int(input("Enter a number: "))
    print(100/number)
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")
except ValueError:
    print("That's not a valid input! Please enter a valid number!")

#Task 2 - Types of Exceptions

#Checking IndexError
check_list = [1,2,3]
try:
    check_list[5]
except IndexError:
    print("IndexError: Your list index is out of range!")

#Checking KeyError
check_key = {"name": "Maggie" }
try:
    print(check_key["age"])
except KeyError:
    print("KeyError: Key not found in the dictionary!")

#Checking TypeError
check_type = "Hello"
try:
    check_type + 5
except TypeError:
    print("TypeError: Unsupported operand types!")

#Task 3 - Using try...except...else...finally
number_1 = int(input("Enter the first value: "))
number_2 = int(input("Enter the second value: "))

try:
    result = (number_1/number_2)
except ValueError:
    print("That's not a valid input! Please enter a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("The result is", result)
finally:
    print("This block always executes.")
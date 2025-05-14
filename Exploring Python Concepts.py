#Task 1
name = "Maggie"
age = 21
birthday = "August 29, 2003"
astrology = "Virgo"
city = "Los Angeles"
siblings = 2

print(f"Hey everyone, my name is {name}! I'm currently {age} and my birthday is on {birthday}, making me a {astrology}! I am from {city}, and I grew up with {siblings} older siblings.")

#Task 2
#Setting my numerical variables (I randomly chose 20 and 50)
num_1 = 20
num_2 = 50

#This is my addition operator
print("The sum of 20 and 50 is", num_1 + num_2)

#This is my subtraction operator
print("The difference of 50 and 20 is", num_2 - num_1)

#This is my multipication operator
print("The multiplication of 20 and 50 is", num_1 * num_2)

#This is my division operator
print("The division of 20 and 50 is", num_1 / num_2)

#Task 3
number = float(input("Enter a number: "))

if number>0:
    print("This number is positive. Awesome!")
elif number==0:
    print("Zero it is. A perfect balance!")
else:
    print("This number is negative. Better luck next time!")
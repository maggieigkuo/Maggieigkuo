age = int(input("How old are you? "))

#If conditional statement to see if the user if 18 or older, if they are they get a message letting them know they can vote
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
#Else conditional statement to let them know they aren't quite old enough to vote
#Then a code to calculate the amount of years they have left before they can
else:
    X = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {X} more years to make a difference!")


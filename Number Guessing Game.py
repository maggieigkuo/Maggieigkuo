import random
number_to_guess = random.randint(1, 100)
attempts = 0

while attempts < 10:
    number = int(input("Guess the number 👀(between 1 and 100): "))
    attempts += 1

    if number > number_to_guess:
        print("Too high! Try again.")
    elif number < number_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts👏")
        break
else:
    print("Game over! Better luck next time☹️")

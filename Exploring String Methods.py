#Task 1 - String Slicing and Indexing

python = "Python is amazing!"
first_word = python[0:6]
print("First word:", first_word)
amazing = python[10:17]
print("Amazing part:", amazing)
reverse = python[::-1]
print("Reversed string:", reverse)

#Task 2 - String Methods

intro = " hello, python world! "
white = intro.strip()
print(white)
cap = white.capitalize()
print(cap)
rep = white.replace("world", "universe")
print(rep)
up = white.upper()
print(up)

#Task 3 - Check for Palindromes

word = input("Enter a word: ")
reversed_word = word[::-1]

if word == reversed_word:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Nope! '{word}' is not a palindrome, think of another one!")
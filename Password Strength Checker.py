password = input("Enter a password: ")

upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in "@#$" for char in password)
length = len(password) >=8

issues = []

if not length:
    issues.append("at least 8 characters")
if not upper:
    issues.append("one uppercase letter")
if not lower:
    issues.append("one lowercase letter")
if not digit:
    issues.append("one digit")
if not special:
    issues.append("one special character (@, #, $)")

if not issues:
    print("Your password is strong! 💪")
else:
    if len(issues) == 1:
        message = issues[0]
    else:
        message = ", ".join(issues[:-1]) + " and " + issues[-1]
    print(f"Your password needs {message}.")




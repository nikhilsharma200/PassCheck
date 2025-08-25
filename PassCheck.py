import re

def password_strength(password):
    if not password:
        return "Error: Password cannot be empty.", []

    criteria_failed = []

    if len(password) < 8:
        criteria_failed.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        criteria_failed.append("uppercase letter")
    if not re.search(r"[a-z]", password):
        criteria_failed.append("lowercase letter")
    if not re.search(r"\d", password):
        criteria_failed.append("digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        criteria_failed.append("special character")

    strength_score = 5 - len(criteria_failed)

    if strength_score <= 2:
        strength = "Weak"
    elif strength_score == 3 or strength_score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, criteria_failed

# Main program
password = input("Enter your password: ")
strength, failed = password_strength(password)
print("Password Strength:", strength)

if failed:
    print("Improve your password by including:", ", ".join(failed))

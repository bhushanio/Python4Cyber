#Library "regex"
import re

#Function to determine the strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak (too short)"
    if not re.search(r'[A-Z]', password):
        return "Weak (missing uppercase letter)"
    if not re.search(r'[a-z]', password):
        return "Weak (missing lowercase letter)"
    if not re.search(r'[0-9]', password):
        return "Weak (missing number)"
    if not re.search(r'[!@#$%^&*()_+{}:<>?]', password):
        return "Weak (missing special character)"
    return "Strong"

#Test Function
password = input("Enter Password: ") # -- Dynamic input from user
strength = check_password_strength(password)
print(f"Password strength: {strength}")

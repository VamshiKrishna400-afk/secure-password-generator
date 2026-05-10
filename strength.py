import string

def check_strength(password):
    strength = 0
    
    if len(password) >= 12:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


if __name__ == "__main__":
    password = input("Enter password to check: ")
    print("Strength:", check_strength(password))

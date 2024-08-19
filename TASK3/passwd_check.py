import re

def check_password_complexity(password):
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Legth Checking
    if len(password) < min_length:
        print("Password must be at least 8 characters long.")
        return False
    
    # Checking uppercase
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        return False
    
    # Checking lowercase
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Checking digits
    if not has_digit:
        print("Password must contain at least one digit.")
        return False
    
    # Checking other characters
    if not has_special:
        print("Password must contain at least one special character (e.g., !@#$%^&*).")
        return False
    
    print("Password is strong!")
    return True

def main():
    password = input("Enter a password to check its complexity: ")
    check_password_complexity(password)

if __name__ == "__main__":
    main()

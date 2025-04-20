import random
import string
import sys

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                      use_digits=True, use_special_chars=True):
    """Generate a random password with specified complexity."""
    # Initialize character pools
    chars = ""
    
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    # Check if at least one character set is selected
    if not chars:
        print("Error: At least one character set must be selected.")
        return None
    
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

def check_password_strength(password):
    """Check the strength of a password and return a rating."""
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
    # Character variety checks
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    # Rate the password
    if score < 3:
        return "Weak"
    elif score < 5:
        return "Moderate"
    elif score < 7:
        return "Strong"
    else:
        return "Very Strong"

def main():
    print("Password Picker")
    print("===============")
    
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        if num_passwords <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    try:
        length = int(input("Enter password length (8-30): "))
        if length < 8 or length > 30:
            print("Password length should be between 8 and 30.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    print("\nGenerated Passwords:")
    print("--------------------")
    
    for i in range(num_passwords):
        password = generate_password(length, use_uppercase, use_lowercase, 
                                    use_digits, use_special_chars)
        if password:
            strength = check_password_strength(password)
            print(f"{i+1}. {password} - {strength}")
    
    print("\nRemember to store your passwords securely!")

if __name__ == "__main__":
    main()
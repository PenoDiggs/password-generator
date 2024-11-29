import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    """
    Generate a random password based on the specified parameters.

    Args:
        length (int): Length of the password.
        include_uppercase (bool): Include uppercase letters if True.
        include_digits (bool): Include digits if True.
        include_special (bool): Include special characters if True.

    Returns:
        str: The generated password.
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    special_characters = string.punctuation if include_special else ""

    # Combine all selected character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if not all_characters:
        raise ValueError("At least one character type must be selected!")

    # Generate password
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    
    # Get user inputs
    length = int(input("Enter the desired password length (e.g., 12): "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    include_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    include_special = input("Include special characters? (y/n): ").strip().lower() == "y"

    try:
        # Generate and display the password
        password = generate_password(length, include_uppercase, include_digits, include_special)
        print(f"Your generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

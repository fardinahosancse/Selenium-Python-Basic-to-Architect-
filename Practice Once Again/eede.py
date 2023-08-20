import re


def check_password_validity(password):
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least two special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 2:
        return False

    # Check for minimum and maximum length
    if len(password) < 10 or len(password) > 24:
        return False

    return True


# Get user input for the password
user_password = input("Enter a password: ")

# Check password validity
is_valid = check_password_validity(user_password)

if is_valid:
    print("Password is valid.")
else:
    print("Password is not valid.")

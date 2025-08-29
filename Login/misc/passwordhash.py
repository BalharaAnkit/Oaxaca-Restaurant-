#pip install argon2-cffi
import argon2

# Function to hash a password
def hash_password(password):
    # Create an Argon2 password hasher
    hasher = argon2.PasswordHasher()

    # Hash the password
    hashed_password = hasher.hash(password)
    return hashed_password

# Function to verify a password against its hash
def verify_password(password, hashed_password):
    # Create an Argon2 password verifier
    verifier = argon2.PasswordVerifier()

    try:
        # Verify the password
        verifier.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerificationError:
        return False

# Example usage
if __name__ == "__main__":
    # Get password from user input (in real application, get this securely)
    password = input("Enter password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Print the hashed password
    print("Hashed password:", hashed_password)

    # Verify a password against its hash
    password_to_check = input("Enter password to check: ")
    if verify_password(password_to_check, hashed_password):
        print("Password is correct!")
    else:
        print("Password is incorrect.")
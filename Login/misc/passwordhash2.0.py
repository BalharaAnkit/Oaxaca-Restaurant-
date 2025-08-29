import argon2

# Function to hash a password
def hash_password(password):
    # Create Argon2 password hasher with sensible parameters
    hasher = argon2.PasswordHasher(
        time_cost=16, memory_cost=102400, parallelism=8, hash_len=32, salt_len=16
    )

    # Hash password
    hashed_password = hasher.hash(password)
    return hashed_password

# Function to verify a password against its hash
def verify_password(password, hashed_password):
    # Create Argon2 password verifier
    verifier = argon2.PasswordVerifier()

    try:
        # Verify the password
        verifier.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerificationError:
        return False

# Example
if __name__ == "__main__":
    # Get password from user input (From DATABASE when integrated)
    password = input("Enter password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Print the hashed password
    print("Hashed password:", hashed_password)

    # Verify password against its hash
    password_to_check = input("Enter password to check: ")
    if verify_password(password_to_check, hashed_password):
        print("Password is correct!")
    else:
        print("Password is incorrect.")
        
"""
Improvements made over previous version:
Parameter Tuning: Adjusted theparameters (time_cost, memory_cost, parallelism, hash_len, salt_len) for a more suitable balance of security and performance.
Error Handling: Added appropriate exception handling for verification errors.
Sensible Defaults: Removed unnecessary instantiation parameters.
Consistency: Made parameter names consistent between functions.

To be integrated with DB in SPRINT 4
"""
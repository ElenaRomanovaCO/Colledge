import random
import string


def generate_otp(length=7):
    """
    Generate a random OTP of the specified length.
    Args: length (int): The desired length of the OTP (default is 6).
    Returns: str: The generated OTP.
    """
    # Defining the character set for the OTP
    characters = string.ascii_letters + string.digits

    # Generating the OTP
    otp = ''.join(random.choice(characters) for _ in range(length))

    return otp

# Usage
otp = generate_otp()
print(f"Your OTP is: {otp}")
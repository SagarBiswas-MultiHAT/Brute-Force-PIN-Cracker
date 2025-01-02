"""
Write a Python script to breach a fictional secure system by guessing a 4-digit PIN code. The PIN code will be randomly generated, and you'll need to use a brute-force approach to crack it.

Constraints:

1. The PIN code consists of 4 digits (0-9).
2. The script should iterate through all possible combinations (0000-9999) to guess the correct PIN.
3. When the correct PIN is guessed, the script should exit and display the correct PIN.

Mock System Response:

To simulate the secure system, I'll respond to your script's attempts with either "ACCESS DENIED" (if the PIN is incorrect) or "SYSTEM BREACHED" (if the PIN is correct).
"""

import random

# Mock system setup: Randomly generate a 4-digit PIN code
actual_pin = f"{random.randint(0, 9999):04d}"

def attempt_pin(guess):
    """
    Simulates the system response to a PIN guess.
    Returns "ACCESS DENIED" if the guess is incorrect,
    and "SYSTEM BREACHED" if the guess is correct.
    """
    if guess == actual_pin:
        return "SYSTEM BREACHED"
    else:
        return "ACCESS DENIED"

# Brute-force attack: Try all possible 4-digit PINs
for pin in range(10000):  # 0000 to 9999
    guess = f"{pin:04d}"  # Format the PIN as a 4-digit string
    response = attempt_pin(guess)
    print(f"Trying PIN: {guess} - {response}")
    
    if response == "SYSTEM BREACHED":
        print(f"Correct PIN found: {guess}")
        break
    
"""
actual_pin = f"{random.randint(0, 9999):04d}" 
04d --- what is it???


The 04d is a formatting directive in Python's f-string that is used to format numbers. Here's what it does:

0: Pads the number with leading zeros if it's shorter than 4 digits.
4: Ensures that the output will be 4 characters long.
d: Stands for "decimal integer," meaning the number will be treated as an integer and displayed as a base-10 number.
In this context, f"{random.randint(0, 9999):04d}" does the following:

random.randint(0, 9999): Generates a random integer between 0 and 9999.
:04d: Formats the number to ensure it is exactly 4 digits long, padding with leading zeros if necessary.
For example:

If the random number is 42, it will be formatted as "0042".
If the random number is 7, it will be formatted as "0007".
If the random number is 1234, it will remain "1234".
This ensures that all PIN codes are exactly 4 digits long, which is important for consistency in your brute-force script.

"""
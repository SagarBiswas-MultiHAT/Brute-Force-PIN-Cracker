# Brute-Force PIN Cracker

## Overview

Welcome to the **Brute-Force PIN Cracker** project! This is a Python script that simulates a brute-force attack to guess a randomly generated 4-digit PIN code. The script attempts all possible combinations of 4 digits (from 0000 to 9999) until it finds the correct one. The mock system responds with either "ACCESS DENIED" or "SYSTEM BREACHED" based on the guessed PIN.

## Features

- Simulates a brute-force attack to crack a 4-digit PIN code.
- Iterates through all possible combinations (0000-9999).
- Provides feedback for each guess, displaying either "ACCESS DENIED" or "SYSTEM BREACHED".
- Once the correct PIN is guessed, the script exits and prints the successful guess.

## How to Run

To run the script, ensure you have Python 3.x installed on your machine.

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Brute-Force-PIN-Cracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Brute-Force-PIN-Cracker
   ```

3. Run the script:

   ```bash
   python pin_cracker.py
   ```

4. The script will begin attempting all PIN combinations, printing the result for each guess until the correct PIN is found.

## How It Works

- The script generates a random 4-digit PIN.
- It then simulates guessing every possible PIN, from 0000 to 9999.
- After each guess, the mock system responds:
  - If the guess is correct, the response is "SYSTEM BREACHED" and the script exits, displaying the correct PIN.
  - If the guess is incorrect, the response is "ACCESS DENIED".
- The process continues until the correct PIN is guessed.

### Example Output:

```
Trying PIN: 0000 - ACCESS DENIED
Trying PIN: 0001 - ACCESS DENIED
Trying PIN: 0002 - ACCESS DENIED
...
Trying PIN: 1234 - SYSTEM BREACHED
Correct PIN found: 1234
```

## Code Explanation

The key part of the script is the use of the brute-force method to generate all possible 4-digit combinations using a `for` loop:

```python
for pin in range(10000):
    guess = f"{pin:04d}"  # Formats the PIN as a 4-digit string
    response = attempt_pin(guess)
    print(f"Trying PIN: {guess} - {response}")
    
    if response == "SYSTEM BREACHED":
        print(f"Correct PIN found: {guess}")
        break
```

The PIN is formatted using the `04d` formatting directive, ensuring that each guess is exactly 4 digits long, even if the number is less than 4 digits.

## Contributions

Feel free to fork the repository and contribute! You can:

- Fix bugs or issues.
- Enhance the brute-force logic or improve the simulation.
- Add features like logging or progress indicators.
- Improve code readability or performance.

To contribute, please fork the repository, make your changes, and create a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Thank you for checking out the **Brute-Force PIN Cracker**. Enjoy experimenting with the code and feel free to reach out with any suggestions or feedback!
```

This `README.md` provides a clear explanation of the project, how to run the script, and how it works, maintaining an approachable, human-written tone throughout.

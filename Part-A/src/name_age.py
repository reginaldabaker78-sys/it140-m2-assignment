"""The program calculates an approximate birth year.

Input:
    The user's name is a srring that comes from the user.
    The user's age is an integer that comes from the user.
    The current calendar year is an integer that comes from the computer.

Process:
    The program subtracts the user's age from the current year to get the approximate birth year.

Output:
    The program displays a string message with the user's name and approximate birth year on the console.

Typical usage example:
    What is your name? Mason
    How old are you? 11
    Hello Mason! You werew born in 2015.
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.

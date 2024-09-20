"""Guessing a simple number."""

__author__ = "730749279"


def guess_a_number() -> None:
    guess = 7  # Unsure to add int but 7 is an int type.
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))

    if x == guess:
        print("You got it!")
    elif x < guess:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()

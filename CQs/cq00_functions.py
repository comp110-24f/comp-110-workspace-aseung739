"""Writing Functions for a Challenge Question."""

__author__ = "730749279"


def mimic(message: str) -> str:
    """Returning a message back."""
    return message


def main() -> None:
    """Printing the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()

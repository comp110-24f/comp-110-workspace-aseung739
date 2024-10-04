"""Implementing Advanced Strings to Imitate Wordle."""

__author__ = "730749279"


def input_guess(secret_word_len: int) -> str:
    """Asking the audience to enter a word with a specific amount of characters."""
    while True:
        # By having the condition True, the while loop continues on.
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
            # By returning guess, the while loop is not entered anymore.
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Identifying if a character exists within the selected word."""
    assert len(char_guess) == 1
    # Line 20 ensures the character guess is one character only.
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Displays the audience a string of emojis to show if their guess is on par with the secret word."""
    assert len(guess) == len(secret)
    # Line 32 ensures the length of the chosen guess and secret are the same.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # In lines 35-37, the variable's initial values do not alter.
    emoji_display: str = ""
    idx: int = 0
    # Just as the idx was initalized at 0, the emoji_display is a string.
    # So, its initalized value is "".
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_display += GREEN_BOX
            # We do not redefine emoji_display, rather we add on to its initalized value.
        elif contains_char(secret, guess[idx]):
            emoji_display += YELLOW_BOX
        else:
            emoji_display += WHITE_BOX
        idx += 1
        # Line 49 ensures all characters of the guess are looped through.
    return emoji_display


def main(secret: str) -> None:
    """Bringing together functions to handle the progression of the game."""
    allowed_turns = 6
    turn = 1
    # Initalize the turn variable with 1, because that is their first attempt.
    while turn <= allowed_turns:
        print(f" === Turn {turn}/{allowed_turns} ===")
        guess = input_guess(len(secret))
        # Line 62 calls back the input_guess function.
        result = emojified(guess, secret)
        print(result)
        # Line 65 calls back the emojified function.
        # Now, we need to create code for when users find the secret_word.
        if guess == secret:
            print(f"You won in {turn}/{allowed_turns} turns!")
            return
            # Line 70 allows the user to exit the game after winning.
        turn += 1
        # Line 72 adds on to the turns until turn <= allowed_turns is False.
    if turn > allowed_turns:
        print(f"X/{allowed_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

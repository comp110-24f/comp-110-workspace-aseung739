"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730749279"


def input_word() -> str:
    user_selected_word = str(input("Enter a 5-character word: "))
    if len(user_selected_word) == 5:
        return user_selected_word
        # Struggled to understand significance of a return statement on line 9.
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # exit() should be placed on line 13 because this is only if the len(user_selected_word) != 5


def input_letter() -> str:
    user_selected_letter = str(input("Enter a single character: "))
    if len(user_selected_letter) == 1:
        return user_selected_letter
    else:
        print("Error: character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    # Code did not run because I did not declare count's type and initial value.
    print("Searching for " + letter + " in " + word)
    # Code does not need str(letter) or str(word) because they were already defined as str.
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
        # Must remember to redefine the value of count when the condition of the if statement is true.
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
        # Needed to remember that strings can concanate together.
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
        # count needs to be turned into a str because it used to be an int.


def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)
    # Struggled in how to call the different function definitions.
    # Line 62 helps call back the input_word and input_letter function definitions.


if __name__ == "__main__":
    main()

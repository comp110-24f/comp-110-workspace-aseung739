"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730749279"


def input_word() -> str:
    user_selected_word = str(input("Enter a 5-character word: "))
    if len(user_selected_word) == 5:
        return user_selected_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_selected_word


def input_letter() -> str:
    user_selected_letter = str(input("Enter a single character: "))
    if len(user_selected_letter) == 1:
        return user_selected_letter
    else:
        print("Error: character must be a single character.")
        return user_selected_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    print("Searching for " + str(letter) + "in " + str(word))
    if word[0] == letter:
        print(str(letter) + " found at index 0")
    if word[1] == letter:
        print(str(letter) + " found at index 1")
    if word[2] == letter:
        print(str(letter) + " found at index 2")
    if word[3] == letter:
        print(str(letter) + " found at index 3")
    if word[4] == letter:
        print(str(letter) + " found at index 4")
        if count == 0:
            print("No instances of " + str(letter) + "found in " + str(word))
        elif count == 1:
            print("1 instance of " + str(letter) + "found in " + str(word))
        else:
            print(str(count) + " instances of " + str(letter) + "found in " + str(word))


def main() -> None:
    contains_char(word=input_word)
    letter = input_letter


if __name__ == "__main__":
    main()

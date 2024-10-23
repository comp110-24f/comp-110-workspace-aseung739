"""Constructing Different Functions to Get Practice with Dictionaries."""

__author__ = "730749279"


def invert(selected_dict: dict[str, str]) -> dict[str, str]:
    """Dictionary that inverts keys and values."""
    outcome: dict[str, str] = {}
    # Line 7 uses curly brackets to create an empty dict.
    for key, value in selected_dict.items():
        if value in outcome:
            # Remember that you can have same values but not same keys.
            raise KeyError("Inverting the dictionary found duplicate keys.")
        outcome[value] = key
    return outcome


def favorite_color(names_and_fav_colors: dict[str, str]) -> str:
    """Finds the most frequently occuring color."""
    color_appearance: dict[str, int] = {}
    # Line 17 also uses curly brackets to create an empty dict.
    # The dict's value was previoously a str, needs to be changed to an int.
    for color in names_and_fav_colors.values():
        if color in color_appearance:
            color_appearance[color] += 1
        else:
            color_appearance[color] = 1
    highest_count: int = 0
    favorite_color: str = ""
    for color in names_and_fav_colors.keys():
        # This ensures the keys are iterated through.
        if color_appearance[names_and_fav_colors[color]] > highest_count:
            highest_count = color_appearance[names_and_fav_colors[color]]
            favorite_color = names_and_fav_colors[color]
    return favorite_color


def count(frequency_list: list[str]) -> dict[str, int]:
    """Finds the number of times a value is in the input list."""
    outcome: dict[str, int] = {}
    # Again, the dict's value was previously a str.
    # The dict's value needs to be an int to follow later code.
    for x in frequency_list:
        if x in outcome:
            outcome[x] += 1
        else:
            outcome[x] = 1
    return outcome


def alphabetizer(words_to_categorize_list: list[str]) -> dict[str, list[str]]:
    """Produces unique keys of the alphabet and the value is a word starting with that letter."""
    outcome: dict[str, list[str]] = {}
    # I initally did not specify outcome with a type.
    # Type must be specified because it should be a dict.
    for x in words_to_categorize_list:
        starting_letter = x[0].lower()
        if starting_letter in outcome:
            outcome[starting_letter].append(x)
        else:
            outcome[starting_letter] = [x]
    return outcome


def update_attendance(
    existing_dict: dict[str, list[str]], day_of_week: str, attended_student: str
) -> None:
    """Mutates and returns the dictionary to update student attendance during the week."""
    if day_of_week in existing_dict:
        # I need to ensure a student is not added on the same day.
        if attended_student not in existing_dict[day_of_week]:
            # Changed if in statement of x to update_attendance.
            existing_dict[day_of_week].append(attended_student)
    else:
        existing_dict[day_of_week] = [attended_student]

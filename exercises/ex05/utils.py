"""Guessing a simple number."""

__author__ = "730749279"


def only_evens(inputted_list: list[int]) -> list[int]:
    """Returns a new list."""
    return [x for x in inputted_list if x % 2 == 0]


def sub(inputted_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Ensures subset value of inputted list."""
    if start_index < 0:
        start_index = 0
        # Line 14 ensures the start_index is not a negative value.
    if end_index > len(inputted_list):
        end_index = len(inputted_list)
        # Line 17 ensures the index does not go out of bounds.
    return inputted_list[start_index:end_index]


def add_at_index(
    inputted_list: list[int], added_element: int, added_index: int
) -> None:
    """Tests if an index is out of bounds."""
    if added_index > len(inputted_list) or added_index < 0:
        raise IndexError("Index is out of bounds for the input list.")
    inputted_list.append(0)
    # Line 28 acts as a new placeholder addition to the list.
    for x in range(len(inputted_list) - 1, added_index, -1):
        inputted_list[x] = inputted_list[x - 1]
    inputted_list[added_index] = added_element

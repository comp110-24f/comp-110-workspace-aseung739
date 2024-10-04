"""Mutating, comparing values, and extending lists of integers."""

__author__ = "730749279"


def all(list_elements: list[int], int_value: int) -> bool:
    """Takes a list of any length and determines if selected numbers are in a specific number."""
    if len(list_elements) == 0:
        return False
    index: int = 0
    # Needed to initalize index on line 11.
    while index != len(list_elements):
        # Changed line 13's operand from != to <.
        # This is because index may go over or under values of len(list_elements).
        if list_elements[index] != int_value:
            return False
        index += 1
    return True
    # Code was not returning anything because a return statement was not included.
    # Thus, line 19 needed to be added.


def max(input: list[int]) -> int:
    """Indicates which value in the list is the largest integer."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_integer: int = input[0]
    index: int = 1
    # Remember that lines 28 and 29's variables are locaally defined.
    while index < len(input):
        if input[index] > largest_integer:
            largest_integer = input[index]
        index += 1
    return largest_integer


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Takes two lists and determines if every element at every specific index is equal."""
    if len(first_list) != len(second_list):
        return False
    index: int = 0
    while index < len(first_list):
        if first_list[index] != second_list[index]:
            return False
        index += 1
        # Line 46 must be added to keep the if statement within the while loop.
    return True
    # Similar to the all function error, a return statement was not included.
    # Thus, line 48 needed to be added.


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Mutates one list using appendation of another list."""
    index: int = 0
    while index < len(second_list):
        first_list.append(second_list[index])
        index += 1
    # This function does not need a return statement like the previous functions.
    # This is due to the function definition specifying no return value.

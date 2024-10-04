"""Mutating functions."""

__author__ = "730749279"


def manual_append(list_of_integers: list[int], int_value: int) -> None:
    """Function mutating its input by appending specific int."""
    list_of_integers[len(list_of_integers) :] = [int_value]


def double(list_of_integers: list[int]) -> None:
    """Function mutating its input by looping through a list."""
    index: int = 0
    while index < len(list_of_integers):
        list_of_integers[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)

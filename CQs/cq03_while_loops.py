"""Searching characters in a phrase."""

__author__ = "730749279"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
    return count

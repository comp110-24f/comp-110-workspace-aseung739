"""Describe it."""

__author__ = "730749279"


def concat(str_value_1: str, str_value_2: str) -> str:
    return str_value_1 + str_value_2


word1: str = "happy"
word2: str = "tuesday"

print(concat("happy", "tuesday"))

if __name__ == "__main__":
    print(concat(word1, word2))

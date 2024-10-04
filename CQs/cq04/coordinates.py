"""Describe it."""

__author__ = "730749279"


def get_coords(xs: str, ys: str) -> None:
    index_1: int = 0
    while index_1 < len(xs):
        index_2: int = 0
        while index_2 < len(ys):
            print(f"({xs[index_1]}, {ys[index_2]})")
            index_2 += 1
        index_1 += 1

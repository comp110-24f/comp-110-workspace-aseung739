"""Summing the elements of a list using different loops."""

__author__ = "730749279"


def w_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns its sum via a while loop."""
    idx: int = 0
    # Remember to initalize the idx at zero!
    sum_amount: float = 0.0
    while idx < len(vals):
        sum_amount += vals[idx]
        idx += 1
    return sum_amount


def f_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns its sum via a for... in... loop."""
    sum_amount: float = 0.0
    for val in vals:
        sum_amount += val
    return sum_amount


def f_range_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns its sums via a for... in range... loop."""
    sum_amount: float = 0.0
    for idx in range(len(vals)):
        sum_amount += vals[idx]
    return sum_amount

from find_max import find_and_remove_max

"""Testing the find_and_remove_max function."""

__author__ = "730749279"


def test_returning_expected_value() -> None:
    "Attempts to return the expected value."
    nums: list[int] = [1, 2, 3, 4, 5]
    result = find_and_remove_max(nums)
    assert result == 5


def test_mutates_input() -> None:
    "Attempts to mutate the input in an expected way."
    nums: list[int] = [2, 4, 4, 4, 2, 2]
    find_and_remove_max(nums)
    assert nums == [2, 2]


def test_edge_case_empty_list() -> None:
    "Attempts to return the correct value when exposed to unconventional values."
    nums: list[int] = []
    result = find_and_remove_max(nums)
    assert result == -1
    assert nums == []

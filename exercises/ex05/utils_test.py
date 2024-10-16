from exercises.ex05.utils import only_evens, sub, add_at_index

"""Guessing a simple number."""

__author__ = "730749279"

# The three functions from lines 9 to 19 test only_evens.


def test_only_evens_empty_list() -> None:
    """Testing an empty list."""
    assert only_evens([]) == []
    # Line 12 ensures the empty list is the expected output.


def test_only_evens_with_even_elements() -> None:
    "Testing a list of only even numbers."
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]
    # Line 18 ensures the list is the same as the outputted list.


def test_only_evens_without_even_elements() -> None:
    "Testing a list of only odd numbers."
    assert only_evens([1, 3, 5, 7]) == []
    # Due to the list being comprised of odd numbers, the list is zero.


# The three functions from lines 26 to 36 test sub.


def test_sub_with_allowable_indices() -> None:
    """Testing the sub function with allowable start and end indices."""
    assert sub([10, 20, 30], 0, 2) == [10, 20]
    # Line 33 showcases a sublist starting from index 0 to 1.


def test_sub_with_equivalent_start_and_end_indices() -> None:
    """Testing sub function when start and end indices are equal."""
    assert sub([10, 20, 30], 1, 1) == []
    # On line 39, the outputted list is empty because of the lack of range definition.


def test_sub_of_one_element() -> None:
    """Testing the sub of start and end indices referencing one element."""
    assert sub([10, 20, 30], 2, 3) == [30]


# The three functions from lines 46-62 test add_at_index


def test_add_at_index_starting_element() -> None:
    """Testing an element added to the start of the list."""
    list: int = [2, 3, 4]
    add_at_index(list, 1, 0)
    assert list == [1, 2, 3, 4]


def test_add_at_index_of_empty_list() -> None:
    """Testing adding an index 0 if with empty list."""
    list: int = []
    add_at_index(list, 1, 0)
    assert list == [1]
    # This ensures the new element is the only element in the list.


def test_add_at_index_of_one_element() -> None:
    """Test adding an element to a list of one element."""
    list: int = [1]
    add_at_index(list, 2, 1)
    assert list == [1, 2]
    # Line 70 ensures the added element comes after previous elements.

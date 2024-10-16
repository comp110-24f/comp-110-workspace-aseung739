"""Takes a list of integers and finds the largest number from the elements."""

__author__ = "730749279"


def find_and_remove_max(nums: list[int]) -> int:
    """Testing that find_and_remove_max returns the expected value."""
    if not nums:
        return -1
    largest_value = max(nums)
    while largest_value in nums:
        # Line 11 removes the largest number via pop.
        nums.remove(largest_value)
    return largest_value

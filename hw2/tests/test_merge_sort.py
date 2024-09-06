"""Test the functionality of merge_sort function."""

from ..hw2_debugging import merge_sort


def test_random_arr():
    """Test the merge_sort function with a random array."""
    arr = [4, 52, 6, 43, 62, 5, 8, 1]

    assert merge_sort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]


def test_already_sorted():
    """Test the merge_sort function with an already sorted array."""
    arr = [1, 4, 5, 6, 8, 43, 52, 62]

    assert merge_sort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]


def test_reverse_sorted():
    """Test the merge_sort function with a reverse sorted array."""
    arr = [62, 52, 43, 8, 6, 5, 4, 1]

    assert merge_sort(arr) == [1, 4, 5, 6, 8, 43, 52, 62]

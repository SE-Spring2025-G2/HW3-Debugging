import pytest
from hw2_debugging import merge_sort 


def test_merge_sort_large_list():
    """Test merge_sort with a large random list."""
    import random
    arr = random.sample(range(100000), 10000)  # 10,000 unique random numbers
    expected = sorted(arr)  # Python's built-in sort for validation
    assert merge_sort(arr) == expected


def test_merge_sort_negative_numbers():
    """Test merge_sort with negative and positive numbers."""
    arr = [-5, 3, -1, 0, -8, 7, 2, -3, 6]
    expected = sorted(arr)
    assert merge_sort(arr) == expected


def test_merge_sort_floats():
    """Test merge_sort with a list containing floating-point numbers."""
    arr = [3.1, 2.4, 5.6, 1.2, 4.9, 3.7]
    expected = sorted(arr)
    assert merge_sort(arr) == expected

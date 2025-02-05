from hw2_debugging import merge_sort

def test_empty_list():
    '''Test empty list edge case'''
    assert merge_sort([]) == []

def test_odd_length():
    '''Test array with odd number of elements'''
    assert merge_sort([5, 3, 1]) == [1, 3, 5]

def test_even_length():
    '''Test array with even number of elements'''
    assert merge_sort([8, 2, 5, 3]) == [2, 3, 5, 8]

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

def test_merge_sort_if_sorted():
    """Test the merge sort function"""
    arr = [1, 2, 3, 4, 5]
    expected = sorted(arr)
    assert merge_sort(arr) == expected

def test_merge_sort_duplicate_values():
    """Test the merge sort function with duplicate values"""
    arr = [11, 2, 7, 11, 4]
    expected = sorted(arr)
    assert merge_sort(arr) == expected

def test_merge_sort_reverse_order():
    """Test the merge sort function with values in reverse order"""
    arr = [5, 4, 3, 2, 1]
    expected = sorted(arr)
    assert merge_sort(arr) == expected

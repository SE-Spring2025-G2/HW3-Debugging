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
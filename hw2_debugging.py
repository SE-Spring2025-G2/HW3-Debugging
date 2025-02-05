"""
Module for the different sorting functions.
"""
import rand

def merge_sort(merge_sort_arr):
    """
    Recursively sorts an array using the merge sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    # Base case: If the array has only one element, it is already sorted
    if len(merge_sort_arr) == 1:
        return merge_sort_arr

    # Calculate the middle index of the array
    half = len(merge_sort_arr) // 2

    # Recursively sort the left and right halves and merge them
    return recombine(merge_sort(merge_sort_arr[:half]), merge_sort(merge_sort_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: The merged sorted array.
    """
    # Initialize indices for the left and right arrays
    left_index = 0
    right_index = 0

    # Create a new array to store the merged result
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    # Merge smaller elements first
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            # Place the smaller element from the left array
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1  # Increment the left index
        else:
            # Place the smaller element from the right array
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1  # Increment the right index

    # Append any remaining elements from the right array
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]  # Corrected index

    # Append any remaining elements from the left array
    for i in range(left_index, len(left_arr)):
        merge_arr[right_index + i] = left_arr[i]  # Corrected index

    return merge_arr


def bubble_sort(bubble_sort_arr):
    """Function to use bubble sort"""

    n = len(bubble_sort_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if bubble_sort_arr[j] > bubble_sort_arr[j+1]:
                bubble_sort_arr[j], bubble_sort_arr[j+1] = bubble_sort_arr[j+1], bubble_sort_arr[j]
    return bubble_sort_arr


arr = rand.random_array([0] * 20)
arr_out = merge_sort(arr)

print(arr_out)

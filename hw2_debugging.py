# Import the random module for generating random arrays
"""
Module for debugging and testing sorting algorithms.

This module contains implementations of merge sort and selection sort algorithms.
It also includes functions for generating random arrays and testing these algorithms.
"""

import secrets

def merge_sort(arr):
    """
    Recursively sorts an array using the merge sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    # Base case: If the array has only one element, it is already sorted
    if len(arr) == 1:
        return arr

    # Calculate the middle index of the array
    half = len(arr) // 2

    # Recursively sort the left and right halves and merge them
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


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


def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    # Get the length of the array
    n = len(arr)

    # Iterate through the array to find the minimum element in each pass
    for i in range(n - 1):
        # Assume the current element is the minimum
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # Update the minimum index if a smaller element is found
                min_index = j

        # Swap the current element with the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Generate a random array of 20 elements
my_array = [secrets.randbelow(101) for _ in range(20)]

# Sort the array using merge sort
arr_out = merge_sort(my_array)

# Print the sorted array
print(arr_out)

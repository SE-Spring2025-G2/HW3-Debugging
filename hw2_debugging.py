"""
Module for the random number functions.
"""
import rand

def merge_sort(merge_sort_arr):
    """Function to use merge sort"""

    if len(merge_sort_arr) == 1:
        return merge_sort_arr

    half = len(merge_sort_arr)//2

    return recombine(merge_sort(merge_sort_arr[:half]), merge_sort(merge_sort_arr[half:]))

def recombine(left_arr, right_arr):
    """Function to recombine the arrays"""

    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr

def bubble_sort(bubble_sort_arr):
    """Function to use bubble sort"""

    n = len(bubble_sort_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if bubble_sort_arr[j] > bubble_sort_arr[j+1]:
                bubble_sort_arr[j], bubble_sort_arr[j+1] = bubble_sort_arr[j+1], bubble_sort_arr[j]
    return bubble_sort_arr


arr = rand.random_array([None] * 20)
arr_out = bubble_sort(arr)

print(arr_out)

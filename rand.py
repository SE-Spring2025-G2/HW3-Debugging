"""
Module for making random number generators
"""
import secrets

def random_array(arr):
    """Function to generate random array without subprocess"""

    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr

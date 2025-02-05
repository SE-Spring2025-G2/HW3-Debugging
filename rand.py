"""
Module for generating random arrays using the `shuf` command.

This module contains a function to generate a random array by shuffling numbers.
"""

import secrets


def random_array(arr):
    """
    Generates a random array by shuffling numbers using the `shuf` command.

    Args:
        arr (list): The input array to be filled with random numbers.

    Returns:
        list: The array filled with random numbers.
    """
    # Iterate through each element in the array
    for i, _ in enumerate(arr):
        # Use subprocess to run the `shuf` command and generate a random number
        # The command shuffles numbers from 1 to 20 and outputs one number
        shuffled_num = [secrets.randbelow(101) for _ in range(20)]
        # Convert the output to an integer and assign it to the array
        arr[i] = int(shuffled_num.stdout.decode().strip())  # Decode and strip the output
    return arr


# Example usage
if __name__ == "__main__":
    # Create an empty array of size 20
    my_arr = [None] * 20
    # Fill the array with random numbers
    random_arr = random_array(my_arr)
    # Print the generated random array
    print(random_arr)

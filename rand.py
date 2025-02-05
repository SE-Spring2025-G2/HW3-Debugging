"""
Module for making random number generators
"""
import secrets

def random_array(arr):
    """Function to generate random array without subprocess"""

    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr


# Example usage
if __name__ == "__main__":
    # Create an empty array of size 20
    my_arr = [None] * 20
    # Fill the array with random numbers
    random_arr = random_array(my_arr)
    # Print the generated random array
    print(random_arr)

"""
Module for importing subprocesses
"""
import subprocess

def random_array(arr):
    """Function to generate random array"""

    shuffled_num = None
    for i, sorted_arr in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        sorted_arr[i] = int(shuffled_num.stdout)
    return arr

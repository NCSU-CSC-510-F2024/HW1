"""Generate an array of random numbers"""
import subprocess


def random_array(arr):
    """Fill an array with random numbers."""
    shuffled_num = None
    for i, _ in range(enumerate(arr)):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
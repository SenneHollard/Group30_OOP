import numpy as np


def add_two_integer_lists(a: list[int], b: list[int]) -> list[int]:
    """Add two lists of integers element-wise."""
    arr = np.array(a) + np.array(b)
    print(f"My added array: {arr}")
    return arr.tolist()


if __name__ == "__main__":
    add_two_integer_lists([1, 2, 3], [4, 5, 6])

# Test

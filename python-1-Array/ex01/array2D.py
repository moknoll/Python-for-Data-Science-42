import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """This function takes a 2D list, a start and endpoint
    and returns the sliced list."""

    try:
        # Check input type
        if not isinstance(family, list):
            raise TypeError("Input must be a list")

        # Convert list to numpy array
        arr = np.array(family)

        # Check if array is 2D
        if arr.ndim != 2:
            raise ValueError("Input must be a 2D array")

        # Check start and end types
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end must be integers")

        print(f"My shape is : {arr.shape}")

        # Slice the array
        sliced_arr = arr[start:end]

        print(f"My new shape is : {sliced_arr.shape}")

        return sliced_arr.tolist()

    except (TypeError, ValueError) as error:
        print(type(error).__name__ + ":", error)
        return []

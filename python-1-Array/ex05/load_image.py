import matplotlib.image as image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path and check if it is JPG or JPEG.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Loaded image.
    """

    try:
        # Check if path is a string
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        # Open image
        img = image.imread(path)

        # Check image format
        if img.format not in ("JPEG", "JPG"):
            raise ValueError("Image must be JPG or JPEG")

        # Convert image to numpy array
        # arr = np.array(img)
        # print(f"The shape of the image is: {arr.shape}")
    except Exception as error:
        print(Exception.__name__ + ":", error)
    return img

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

        # Convert image to RGB
        img = img.convert("RGB")

        # Convert image to numpy array
        arr = np.array(img)

        print(f"The shape of the image is: {arr.shape}")
    except Exception as error:
        print(Exception.__name__ + ":", error)
    else:
        return arr

    return img


def zoom(img: np.ndarray) -> np.ndarray:
    """
    Crop and display a portion of the given image.

    Args:
        img (np.ndarray): Input image as a NumPy array.

    Returns:
        None
    """

    cropped = img[0:400, 400:800].copy()

    # Display the scale on the x and y axis on the image
    print(f"New shape after slicing : {cropped.shape} or {cropped.shape[:2]}")
    # print(cropped)

    return cropped

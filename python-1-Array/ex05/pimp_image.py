import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the RGB colors of the given image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with inverted colors.
    """
    res = array.copy()
    for i, x in enumerate(res):
        for j, y in enumerate(x):
            for k, z in enumerate(y):
                res[i, j, k] = 255 - z
    plt.imshow(res)
    plt.show()
    return res


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Apply a red filter to the given image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with a red filter.
    """
    res = array.copy()
    for i, x in enumerate(res):
        for j, y in enumerate(x):
            res[i, j, 1] = res[i, j, 1] * 0.3
            res[i, j, 2] = res[i, j, 2] * 0.3
    plt.imshow(res)
    plt.show()
    return res


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Apply a green filter to the given image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with a green filter.
    """
    res = array.copy()
    for i, x in enumerate(res):
        for j, y in enumerate(x):
            res[i, j, 0] = 0
            res[i, j, 2] = 0
    plt.imshow(res)
    plt.show()
    return res


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Apply a blue filter to the given image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with a blue filter.
    """
    res = array.copy()
    for i, x in enumerate(res):
        for j, y in enumerate(x):
            res[i, j, 0] = 0
            res[i, j, 1] = 0
    plt.imshow(res)
    plt.show()
    return res


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the given image to grayscale.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Grayscale image.
    """
    res = array.copy()

    for i, x in enumerate(res):
        for j, y in enumerate(x):
            grey = (int(res[i, j, 0]) + int(res[i, j, 1])
                    + int(res[i, j, 2])) / 3

            res[i, j, 0] = grey
            res[i, j, 1] = grey
            res[i, j, 2] = grey

    plt.imshow(res)
    plt.show()
    return res

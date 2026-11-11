from load_image import ft_load, zoom
import matplotlib.pyplot as plt
import numpy as np


def rotate(matrix: np.ndarray) -> None:
    """
    Rotate the given image matrix by 90 degrees counterclockwise.

    Args:
        matrix (np.ndarray): Input image as a NumPy array.

    Returns:
        None
    """
    height, width = matrix.shape[:2]
    rotated = np.empty((width, height, *matrix.shape[2:]),
                       dtype=matrix.dtype)

    for i in range(height):
        for j in range(width):
            rotated[j][height - 1 - i] = matrix[i][j]

    plt.imshow(rotated)
    plt.show()


def main():
    """
    Load an image, crop it, display it and rotate the result.

    Returns:
        None
    """
    img = ft_load("./animal.jpeg")
    cropped = zoom(img)

    plt.imshow(cropped)
    plt.title("Before rotation")
    plt.show()

    rotate(cropped)


if __name__ == "__main__":
    main()

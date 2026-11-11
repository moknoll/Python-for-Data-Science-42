from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(img: np.ndarray) -> None:
    """
    Crop and display a portion of the given image.

    Args:
        img (np.ndarray): Input image as a NumPy array.

    Returns:
        None
    """

    cropped = img[0:600, 400:1000]

    # Display the scale on the x and y axis on the image
    print(f"New shape after slicing : {cropped.shape} or {cropped.shape[:2]}")
    print(cropped)
    plt.imshow(cropped)
    plt.show()
    return


def main():
    img = ft_load("./animal.jpeg")
    zoom(img)


if __name__ == "__main__":
    main()

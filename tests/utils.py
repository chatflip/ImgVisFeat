import cv2
import numpy as np
from numpy.typing import NDArray


def get_test_image_path() -> str:
    """Get the path to the test image.

    Returns:
        str: Path to the test image.
    """
    return "tests/resources/images/test_image.jpg"


def get_test_text_path() -> str:
    """Get the path to the test text.

    Returns:
        str: Path to the test text.
    """
    return "tests/resources/text/test_text.txt"


def get_image(is_gray: bool = False) -> NDArray[np.uint8]:
    """Return Color/Grayscale image.

    Args:
        is_gray (bool, optional): If True, return a grayscale image. Defaults to False.

    Returns:
        NDArray[np.uint8]: Color/Grayscale image.
    """
    image_path = get_test_image_path()
    flag = cv2.IMREAD_GRAYSCALE if is_gray else cv2.IMREAD_COLOR
    return cv2.imread(image_path, flag).astype(np.uint8)

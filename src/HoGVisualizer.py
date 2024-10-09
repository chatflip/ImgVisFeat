import cv2
import numpy as np
from numpy.typing import NDArray
from skimage import feature

from .AbstractVisualizer import AbstractVisualizer
from .type import HogResult


class HoGVisualizer(AbstractVisualizer):
    """A class for visualizing the HoG features of an image."""

    def __init__(self) -> None:
        """Initialize the HoGVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> HogResult:
        """Compute the HoG features of an image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            HogResult: The HoG features of the image.
        """
        if source.ndim != 2:
            gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        else:
            gray = source.copy()
        _, hog_image = feature.hog(
            gray,
            orientations=9,
            pixels_per_cell=(16, 16),
            cells_per_block=(2, 2),
            block_norm="L2-Hys",
            visualize=True,
        )
        hog_image = np.uint8(hog_image * 255)
        return HogResult(hog_image)

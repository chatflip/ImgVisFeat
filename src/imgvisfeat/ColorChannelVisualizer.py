import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import ColorChannelResult


class ColorChannelVisualizer(AbstractVisualizer):
    """A class for splitting the color channels of an image."""

    def __init__(self) -> None:
        """Initialize the ColorChannelVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> ColorChannelResult:
        """Split the color channels of an image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            ColorChannelResult: The blue, green, and red color channels.
        """
        image = source.copy()
        if image.ndim != 3:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR).astype(np.uint8)
        blue = np.zeros_like(image, dtype=np.uint8)
        green = np.zeros_like(image, dtype=np.uint8)
        red = np.zeros_like(image, dtype=np.uint8)
        blue[:, :, 0] = image[:, :, 0]
        green[:, :, 1] = image[:, :, 1]
        red[:, :, 2] = image[:, :, 2]
        return ColorChannelResult(blue, green, red)

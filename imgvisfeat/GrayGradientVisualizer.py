import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import GradientResult


class GrayGradientVisualizer(AbstractVisualizer):
    """A class for computing the gradient of a grayscale image."""

    def __init__(self) -> None:
        """Initialize the GrayGradientVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> GradientResult:
        """Compute the gradient of a grayscale image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            GradientResult: The gradient in the x, y, and xy directions.
        """
        if source.ndim != 2:
            gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        else:
            gray = source.copy()
        kernel_x = np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0]], np.float32)
        kernel_y = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]], np.float32)
        kernel_xy = np.array([[0, 1, 0], [-1, 0, 1], [0, -1, 0]], np.float32)
        grad_x = cv2.filter2D(gray, -1, kernel_x).astype(np.uint8)
        grad_y = cv2.filter2D(gray, -1, kernel_y).astype(np.uint8)
        grad_xy = cv2.filter2D(gray, -1, kernel_xy).astype(np.uint8)
        return GradientResult(grad_x, grad_y, grad_xy)

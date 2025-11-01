import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import GradientResult


class ColorGradientVisualizer(AbstractVisualizer):
    """A class for computing the gradient of a color image."""

    def __init__(self) -> None:
        """Initialize the ColorGradientVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> GradientResult:
        """Compute the gradient of a color image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            GradientResult: The gradient in the x, y, and xy directions.
        """
        image = source.copy()
        if image.ndim != 3:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        grad_x = np.zeros_like(image, dtype=np.uint8)
        grad_y = np.zeros_like(image, dtype=np.uint8)
        grad_xy = np.zeros_like(image, dtype=np.uint8)
        kernel_x = np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0]], np.float32)
        kernel_y = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]], np.float32)
        kernel_xy = np.array([[0, 1, 0], [-1, 0, 1], [0, -1, 0]], np.float32)
        grad_x[:, :, 0] = cv2.filter2D(image[:, :, 0], -1, kernel_x)
        grad_y[:, :, 0] = cv2.filter2D(image[:, :, 0], -1, kernel_y)
        grad_xy[:, :, 0] = cv2.filter2D(image[:, :, 0], -1, kernel_xy)
        grad_x[:, :, 1] = cv2.filter2D(image[:, :, 1], -1, kernel_x)
        grad_y[:, :, 1] = cv2.filter2D(image[:, :, 1], -1, kernel_y)
        grad_xy[:, :, 1] = cv2.filter2D(image[:, :, 1], -1, kernel_xy)
        grad_x[:, :, 2] = cv2.filter2D(image[:, :, 2], -1, kernel_x)
        grad_y[:, :, 2] = cv2.filter2D(image[:, :, 2], -1, kernel_y)
        grad_xy[:, :, 2] = cv2.filter2D(image[:, :, 2], -1, kernel_xy)
        return GradientResult(grad_x, grad_y, grad_xy)


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

import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import PowerSpectrumResult


class PowerSpectrumVisualizer(AbstractVisualizer):
    """A class for computing the power spectrum of an image."""

    def __init__(self) -> None:
        """Initialize the PowerSpectrumVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> PowerSpectrumResult:
        """Compute the power spectrum of an image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            PowerSpectrumResult: The power spectrum of the image.
        """
        if source.ndim != 2:
            gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        else:
            gray = source.copy()
        gray = np.array(gray)
        fft = np.fft.fft2(gray)
        fft = np.fft.fftshift(fft)
        pow = np.abs(fft) ** 2
        pow = np.log10(pow)
        p_max = np.max(pow)
        pow = pow / p_max * 255
        pow_image = np.array(np.uint8(pow))

        return PowerSpectrumResult(pow_image)

import numpy as np
from numpy.typing import NDArray

import imgvisfeat as ivf


def test_hog_visualizer_color(
    power_spectrum_visualizer: ivf.PowerSpectrumVisualizer,
    color_image: NDArray[np.uint8],
) -> None:
    """Test the PowerSpectrumVisualizer class with a color image."""
    result = power_spectrum_visualizer(color_image)
    assert result.power_spectrum.shape == color_image.shape[:2]


def test_hog_visualizer_gray(
    power_spectrum_visualizer: ivf.PowerSpectrumVisualizer,
    gray_image: NDArray[np.uint8],
) -> None:
    """Test the PowerSpectrumVisualizer class with a grayscale image."""
    result = power_spectrum_visualizer(gray_image)
    assert result.power_spectrum.shape == gray_image.shape

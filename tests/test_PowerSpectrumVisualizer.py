import numpy as np
from numpy.typing import NDArray

import ivf


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


def test_power_spectrum_visualizer_str(
    power_spectrum_visualizer: ivf.PowerSpectrumVisualizer,
) -> None:
    """Test the __str__ method of the PowerSpectrumVisualizer class."""
    assert str(power_spectrum_visualizer) == "PowerSpectrumVisualizer"

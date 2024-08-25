import numpy as np
from numpy.typing import NDArray

import imgvisfeat as ivf


def test_hog_visualizer_color(
    hog_visualizer: ivf.HoGVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the HoGVisualizer class with a color image."""
    result = hog_visualizer(color_image)
    assert result.hog.shape == color_image.shape[:2]


def test_hog_visualizer_gray(
    hog_visualizer: ivf.HoGVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the HoGVisualizer class with a grayscale image."""
    result = hog_visualizer(gray_image)
    assert result.hog.shape == gray_image.shape

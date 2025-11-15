import numpy as np
from numpy.typing import NDArray

import ivf


def test_lbp_visualizer_color(
    lbp_visualizer: ivf.LBPVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the LBPVisualizer class with a color image."""
    result = lbp_visualizer(color_image)
    assert result.lbp.shape == color_image.shape[:2]


def test_lbp_visualizer_gray(
    lbp_visualizer: ivf.LBPVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the LBPVisualizer class with a grayscale image."""
    result = lbp_visualizer(gray_image)
    assert result.lbp.shape == gray_image.shape


def test_lbp_visualizer_str(lbp_visualizer: ivf.LBPVisualizer) -> None:
    """Test the __str__ method of the LBPVisualizer class."""
    assert str(lbp_visualizer) == "LBPVisualizer"

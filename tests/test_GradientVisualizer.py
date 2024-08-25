import numpy as np
from numpy.typing import NDArray

import imgvisfeat as ivf


def test_gray_gradient_visualizer_color(
    gray_gradient_visualizer: ivf.GrayGradientVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the GrayGradientVisualizer class with a color image."""
    result = gray_gradient_visualizer(color_image)
    assert result.gradient_x.shape == color_image.shape[:2]
    assert result.gradient_y.shape == color_image.shape[:2]
    assert result.gradient_xy.shape == color_image.shape[:2]


def test_gray_gradient_visualizer_gray(
    gray_gradient_visualizer: ivf.GrayGradientVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the GrayGradientVisualizer class with a color image."""
    result = gray_gradient_visualizer(gray_image)
    assert result.gradient_x.shape == gray_image.shape
    assert result.gradient_y.shape == gray_image.shape
    assert result.gradient_xy.shape == gray_image.shape


def test_color_gradient_visualizer_color(
    color_gradient_visualizer: ivf.ColorGradientVisualizer,
    color_image: NDArray[np.uint8],
) -> None:
    """Test the ColorGradientVisualizer class with a color image."""
    result = color_gradient_visualizer(color_image)
    assert result.gradient_x.shape == color_image.shape
    assert result.gradient_y.shape == color_image.shape
    assert result.gradient_xy.shape == color_image.shape


def test_color_gradient_visualizer_gray(
    color_gradient_visualizer: ivf.ColorGradientVisualizer,
    gray_image: NDArray[np.uint8],
) -> None:
    """Test the ColorGradientVisualizer class with a color image."""
    result = color_gradient_visualizer(gray_image)
    assert result.gradient_x.shape[:2] == gray_image.shape
    assert result.gradient_y.shape[:2] == gray_image.shape
    assert result.gradient_xy.shape[:2] == gray_image.shape


def test_gray_gradient_visualizer_str(
    gray_gradient_visualizer: ivf.GrayGradientVisualizer,
) -> None:
    """Test the __str__ method of the GrayGradientVisualizer class."""
    assert str(gray_gradient_visualizer) == "GrayGradientVisualizer"

def test_color_gradient_visualizer_str(
    color_gradient_visualizer: ivf.ColorGradientVisualizer,
) -> None:
    """Test the __str__ method of the ColorGradientVisualizer class."""
    assert str(color_gradient_visualizer) == "ColorGradientVisualizer"

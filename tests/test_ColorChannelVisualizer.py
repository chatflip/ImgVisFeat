import imgvisfeat as ivf
import numpy as np
from numpy.typing import NDArray


def test_color_channel_visualizer_color(
    color_channel_visualizer: ivf.ColorChannelVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the ColorChannelVisualizer class with a color image."""
    result = color_channel_visualizer(color_image)
    assert result.blue.shape == color_image.shape
    assert result.green.shape == color_image.shape
    assert result.red.shape == color_image.shape


def test_color_channel_visualizer_gray(
    color_channel_visualizer: ivf.ColorChannelVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the ColorChannelVisualizer class with a color image."""
    result = color_channel_visualizer(gray_image)
    assert result.blue.shape[:2] == gray_image.shape[:2]
    assert result.green.shape[:2] == gray_image.shape[:2]
    assert result.red.shape[:2] == gray_image.shape[:2]


def test_color_channel_visualizer_str(
    color_channel_visualizer: ivf.ColorChannelVisualizer,
) -> None:
    """Test the __str__ method of the ColorChannelVisualizer class."""
    assert str(color_channel_visualizer) == "ColorChannelVisualizer"

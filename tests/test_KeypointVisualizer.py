import numpy as np
import pytest
from numpy.typing import NDArray

import imgvisfeat as ivf


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_color(algorithm_name: str, color_image: NDArray[np.uint8]) -> None:
    """Test the KeypointVisualizer class with a color image."""
    visualizer = ivf.KeypointVisualizer(algorithm_name)
    result = visualizer(color_image)
    assert result.keypoint.shape == color_image.shape
    assert result.rich_keypoint.shape == color_image.shape


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_gray(algorithm_name: str, gray_image: NDArray[np.uint8]) -> None:
    """Test the KeypointVisualizer class with a grayscale image."""
    visualizer = ivf.KeypointVisualizer(algorithm_name)
    result = visualizer(gray_image)
    assert result.keypoint.shape[:2] == gray_image.shape
    assert result.rich_keypoint.shape[:2] == gray_image.shape


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_str(algorithm_name: str) -> None:
    """Test the string representation of the KeypointVisualizer class."""
    visualizer = ivf.KeypointVisualizer(algorithm_name)
    assert str(visualizer) == f"KeypointVisualizer({algorithm_name})"


def test_invalid_keypoint_visualizer() -> None:
    """Test the KeypointVisualizer class with an invalid keypoint algorithm."""
    with pytest.raises(ValueError):
        ivf.KeypointVisualizer("INVALID")


def test_sift_visualizer_str(sift_visualizer: ivf.KeypointVisualizer) -> None:
    """Test the __str__ method of the KeypointVisualizer(SIFT) class."""
    assert str(sift_visualizer) == "KeypointVisualizer(SIFT)"


def test_akaze_visualizer_str(akaze_visualizer: ivf.KeypointVisualizer) -> None:
    """Test the __str__ method of the KeypointVisualizer(AKAZE) class."""
    assert str(akaze_visualizer) == "KeypointVisualizer(AKAZE)"


def test_orb_visualizer_str(orb_visualizer: ivf.KeypointVisualizer) -> None:
    """Test the __str__ method of the KeypointVisualizer(ORB) class."""
    assert str(orb_visualizer) == "KeypointVisualizer(ORB)"

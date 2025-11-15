import numpy as np
import pytest
from numpy.typing import NDArray

import imfv


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_color(algorithm_name: str, color_image: NDArray[np.uint8]) -> None:
    """Test the KeypointVisualizer class with a color image."""
    visualizer = imfv.KeypointVisualizer(algorithm_name)
    result = visualizer(color_image)
    assert result.keypoint.shape == color_image.shape
    assert result.rich_keypoint.shape == color_image.shape


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_gray(algorithm_name: str, gray_image: NDArray[np.uint8]) -> None:
    """Test the KeypointVisualizer class with a grayscale image."""
    visualizer = imfv.KeypointVisualizer(algorithm_name)
    result = visualizer(gray_image)
    assert result.keypoint.shape[:2] == gray_image.shape
    assert result.rich_keypoint.shape[:2] == gray_image.shape


@pytest.mark.parametrize("algorithm_name", ["AKAZE", "SIFT", "ORB"])
def test_visualizer_str(algorithm_name: str) -> None:
    """Test the string representation of the KeypointVisualizer class."""
    visualizer = imfv.KeypointVisualizer(algorithm_name)
    assert str(visualizer) == f"KeypointVisualizer({algorithm_name})"


def test_invalid_keypoint_visualizer() -> None:
    """Test the KeypointVisualizer class with an invalid keypoint algorithm."""
    with pytest.raises(ValueError):
        imfv.KeypointVisualizer("INVALID")


def test_invalid_keypoint_visualizer_changed(color_image: NDArray[np.uint8]) -> None:
    """Test the KeypointVisualizer class with an invalid keypoint algorithm."""
    visualizer = imfv.KeypointVisualizer("AKAZE")
    visualizer.algorithm_name = "INVALID"
    with pytest.raises(ValueError):
        visualizer(color_image)

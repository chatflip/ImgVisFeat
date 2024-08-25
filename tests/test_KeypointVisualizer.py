import numpy as np
from numpy.typing import NDArray

import imgvisfeat as ivf


def test_sift_visualizer_color(
    sift_visualizer : ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(SIFT) class with a color image."""
    result = sift_visualizer(color_image)
    assert result.keypoint.shape == color_image.shape
    assert result.rich_keypoint.shape == color_image.shape


def test_sift_visualizer_gray(
    sift_visualizer: ivf.KeypointVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(SIFT) class with a color image."""
    result = sift_visualizer(gray_image)
    assert result.keypoint.shape[:2] == gray_image.shape
    assert result.rich_keypoint.shape[:2] == gray_image.shape

def test_akaze_visualizer_color(
    akaze_visualizer : ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(AKAZE) class with a color image."""
    result = akaze_visualizer(color_image)
    assert result.keypoint.shape == color_image.shape
    assert result.rich_keypoint.shape == color_image.shape


def test_akaze_visualizer_gray(
    akaze_visualizer: ivf.KeypointVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(AKAZE) class with a color image."""
    result = akaze_visualizer(gray_image)
    assert result.keypoint.shape[:2] == gray_image.shape
    assert result.rich_keypoint.shape[:2] == gray_image.shape

def test_orb_visualizer_color(
    orb_visualizer : ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(ORB) class with a color image."""
    result = orb_visualizer(color_image)
    assert result.keypoint.shape == color_image.shape
    assert result.rich_keypoint.shape == color_image.shape


def test_orb_visualizer_gray(
    orb_visualizer: ivf.KeypointVisualizer, gray_image: NDArray[np.uint8]
) -> None:
    """Test the KeypointVisualizer(ORB) class with a color image."""
    result = orb_visualizer(gray_image)
    assert result.keypoint.shape[:2] == gray_image.shape
    assert result.rich_keypoint.shape[:2] == gray_image.shape
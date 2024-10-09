import imgvisfeat as ivf
import numpy as np
import pytest
from numpy.typing import NDArray


def test_sift_visualizer_color(
    sift_visualizer: ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
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
    akaze_visualizer: ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
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
    orb_visualizer: ivf.KeypointVisualizer, color_image: NDArray[np.uint8]
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

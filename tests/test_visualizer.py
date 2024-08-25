from unittest import mock

import pytest

import imgvisfeat as ivf


def get_test_image_path() -> str:
    """Get the path to the test image.

    Returns:
        str: Path to the test image.
    """
    return "tests/resources/images/test_image.jpg"


def get_test_text_path() -> str:
    """Get the path to the test text.

    Returns:
        str: Path to the test text.
    """
    return "tests/resources/text/test_text.txt"


def test_nonexistent_file() -> None:
    """Test Visualizer raises ValueError for nonexistent file.

    Ensures Visualizer.visualize() raises a ValueError when given a
    file path that does not exist.

    Raises:
        ValueError: When a nonexistent file path is provided to visualize().
    """
    vis = ivf.Visualizer()
    non_exists_file_path = "path/to/nonexists/path.jpg"
    with pytest.raises(ValueError):
        vis.visualize(non_exists_file_path)


def test_directory() -> None:
    """Test Visualizer raises ValueError for directory input.

    Ensures Visualizer.visualize() raises a ValueError when given a
    directory path instead of an image file path.

    Raises:
        ValueError: When a directory path is provided to visualize().
    """
    vis = ivf.Visualizer()
    directory_path = "tests/resources/images"
    with pytest.raises(ValueError):
        vis.visualize(directory_path)


def test_text() -> None:
    """Test the visualize method with a text file.

    Raises:
        ValueError: If the text file is not an image.
    """
    vis = ivf.Visualizer()
    text_path = get_test_text_path()
    with pytest.raises(ValueError):
        vis.visualize(text_path)


def test_visualize() -> None:
    """Test Visualizer.visualize() execution flow with mocked cv2 functions.

    Ensures Visualizer.visualize() calls cv2.imshow, cv2.waitKey, and
    cv2.destroyAllWindows in the correct order when given a valid image path.

    Uses mock.patch to replace cv2 functions and verify their calls.
    """
    vis = ivf.Visualizer()
    image_path = get_test_image_path()
    with (
        mock.patch("cv2.imshow"),
        mock.patch("cv2.waitKey", return_value=1),
        mock.patch("cv2.destroyAllWindows"),
    ):
        vis.visualize(image_path)

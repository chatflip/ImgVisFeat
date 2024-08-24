import pytest

import imgvisfeat as ivf


def get_test_image_path() -> str:
    return "tests/resources/images/test_image.jpg"


def get_test_text_path() -> str:
    return "tests/resources/text/test_text.txt"


def test_nonexistent_file() -> None:
    vis = ivf.Visualizer()
    non_exists_file_path = "path/to/nonexists/path.jpg"
    with pytest.raises(ValueError):
        vis.visualize(non_exists_file_path)

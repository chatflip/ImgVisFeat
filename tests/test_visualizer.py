import tempfile

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


def test_directory() -> None:
    vis = ivf.Visualizer()
    directory_path = "tests/resources/images"
    with pytest.raises(ValueError):
        vis.visualize(directory_path)


def test_text() -> None:
    vis = ivf.Visualizer()
    text_path = get_test_text_path()
    with pytest.raises(ValueError):
        vis.visualize(text_path)


def test_run_show() -> None:
    vis = ivf.Visualizer()
    image_path = get_test_image_path()
    vis.visualize(image_path)


def test_run_file() -> None:
    vis = ivf.Visualizer()
    image_path = get_test_image_path()
    with tempfile.TemporaryDirectory() as temp_dir:
        vis.visualize(image_path, dst_root=temp_dir)

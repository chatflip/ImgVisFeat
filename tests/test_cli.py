from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from pytest import CaptureFixture

from imvf import cli

from .utils import get_test_image_path


@pytest.fixture(name="mock_argparse")
def mock_argparse() -> Generator[MagicMock, None, None]:
    """Fixture to mock the ArgumentParser class.

    Yields:
        MagicMock: A mock object representing the ArgumentParser class.
    """
    with patch("argparse.ArgumentParser", autospec=True) as mock:
        parser = mock.return_value
        parser.parse_args = MagicMock()
        yield parser


def test_main_successful_execution(
    mock_argparse: MagicMock, capsys: CaptureFixture[str]
) -> None:
    """Test successful execution of the main CLI function.

    This test ensures that the Visualizer's visualize method is called
    and output is produced when the CLI is executed successfully.

    Args:
        mock_argparse (MagicMock): Mocked ArgumentParser class.
        capsys (CaptureFixture[str]): Pytest fixture to capture stdout and stderr.

    """
    mock_argparse.parse_args.return_value = MagicMock(
        image_path=get_test_image_path(), method="all"
    )
    with (
        patch("cv2.imshow"),
        patch("cv2.waitKey", return_value=1),
        patch("cv2.destroyAllWindows"),
    ):
        with pytest.raises(SystemExit) as exc_info:
            cli.main()
    captured = capsys.readouterr()
    last_line = captured.out.splitlines()[-1]
    assert "Visualization complete." in last_line
    assert exc_info.value.code == 0  # type: ignore[attr-defined]


def test_main_error_handling(mock_argparse: MagicMock) -> None:
    """Test error handling in the main CLI function.

    This test ensures that the CLI function raises an exception
    when an invalid path is provided as an argument.

    Args:
        mock_argparse (MagicMock): Mocked ArgumentParser class.

    """
    mock_argparse.parse_args.return_value = MagicMock(
        image_path="path/to/nonexists/path.jpg", method="all"
    )

    with pytest.raises(SystemExit) as exc_info:
        cli.main()
    assert exc_info.value.code == 1  # type: ignore[attr-defined]

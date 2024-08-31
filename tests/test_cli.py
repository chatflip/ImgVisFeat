from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from pytest import CaptureFixture

from imgvisfeat import cli

from .utils import get_test_image_path


@pytest.fixture
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
        cli.main()
    captured = capsys.readouterr()
    last_line = captured.out.splitlines()[-1]
    assert "Visualization complete." in last_line

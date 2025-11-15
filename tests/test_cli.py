from unittest.mock import patch

import pytest
from pytest import CaptureFixture
from typer.testing import CliRunner

from imvf import cli

from .utils import get_test_image_path


@pytest.fixture(name="cli_runner")
def cli_runner() -> CliRunner:
    """Fixture to create a Typer CliRunner.

    Returns:
        CliRunner: A Typer CliRunner instance for testing.
    """
    return CliRunner()


@pytest.fixture(name="mock_cv2")
def mock_cv2():
    """Fixture to mock cv2 display functions.

    Yields:
        Context manager for cv2 mocks.
    """
    with (
        patch("cv2.imshow"),
        patch("cv2.waitKey", return_value=1),
        patch("cv2.destroyAllWindows"),
    ):
        yield


def test_main_successful_execution(
    cli_runner: CliRunner, capsys: CaptureFixture[str], mock_cv2
) -> None:
    """Test successful execution of the main CLI function.

    This test ensures that the Visualizer's visualize method is called
    and output is produced when the CLI is executed successfully.

    Args:
        cli_runner (CliRunner): Typer CLI runner.
        capsys (CaptureFixture[str]): Pytest fixture to capture stdout and stderr.
        mock_cv2: Fixture for mocking cv2 functions.

    """
    result = cli_runner.invoke(cli.app, ["all", get_test_image_path()])
    assert result.exit_code == 0
    assert "Visualization complete." in result.stdout


def test_main_error_handling(cli_runner: CliRunner) -> None:
    """Test error handling in the main CLI function.

    This test ensures that the CLI function raises an exception
    when an invalid path is provided as an argument.

    Args:
        cli_runner (CliRunner): Typer CLI runner.

    """
    result = cli_runner.invoke(cli.app, ["all", "path/to/nonexists/path.jpg"])
    assert result.exit_code == 1


@pytest.mark.parametrize(
    "subcommand",
    [
        "all",
        "color-channel",
        "gradient",
        "hog",
        "keypoint",
        "lbp",
        "power-spectrum",
    ],
)
def test_all_subcommands_successful(
    cli_runner: CliRunner, mock_cv2, subcommand: str
) -> None:
    """Test that all subcommands execute successfully.

    Args:
        cli_runner (CliRunner): Typer CLI runner.
        mock_cv2: Fixture for mocking cv2 functions.
        subcommand (str): The subcommand to test.

    """
    result = cli_runner.invoke(cli.app, [subcommand, get_test_image_path()])
    assert result.exit_code == 0
    assert "Visualization complete." in result.stdout


@pytest.mark.parametrize(
    "subcommand",
    [
        "all",
        "color-channel",
        "gradient",
        "hog",
        "keypoint",
        "lbp",
        "power-spectrum",
    ],
)
def test_all_subcommands_error_handling(cli_runner: CliRunner, subcommand: str) -> None:
    """Test error handling for all subcommands.

    Args:
        cli_runner (CliRunner): Typer CLI runner.
        subcommand (str): The subcommand to test.

    """
    result = cli_runner.invoke(cli.app, [subcommand, "path/to/nonexists/path.jpg"])
    assert result.exit_code == 1
    # Error messages are written to stderr
    assert "Error:" in result.stderr
    assert "Visualization failed" in result.stderr


def test_help_command(cli_runner: CliRunner) -> None:
    """Test that the help command works.

    Args:
        cli_runner (CliRunner): Typer CLI runner.

    """
    result = cli_runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "ImgVisFeat: Visualize image features" in result.stdout
    assert "all" in result.stdout
    assert "color-channel" in result.stdout
    assert "gradient" in result.stdout
    assert "hog" in result.stdout
    assert "keypoint" in result.stdout
    assert "lbp" in result.stdout
    assert "power-spectrum" in result.stdout


def test_subcommand_help(cli_runner: CliRunner) -> None:
    """Test that subcommand help works.

    Args:
        cli_runner (CliRunner): Typer CLI runner.

    """
    result = cli_runner.invoke(cli.app, ["all", "--help"])
    assert result.exit_code == 0
    assert "Visualize all features" in result.stdout
    assert "IMAGE_PATH" in result.stdout

import sys
from typing import Annotated

import typer

import imvf

app = typer.Typer(help="ImgVisFeat: Visualize image features")


def visualize_image(method: str, image_path: str) -> None:
    """Execute visualization with the specified method.

    Args:
        method: Visualization method to use.
        image_path: Path to the input image.
    """
    visualizer = imvf.Visualizer()
    try:
        visualizer.visualize(image_path)
    except Exception as e:
        typer.echo(f"Error: {str(e)}", err=True)
        typer.echo("Visualization failed.", err=True)
        raise typer.Exit(code=1)
    typer.echo("Visualization complete.")
    sys.exit(0)


@app.command()
def all(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize all features."""
    visualize_image("all", image_path)


@app.command()
def color_channel(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize color channels."""
    visualize_image("color_channel", image_path)


@app.command()
def gradient(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize gradients."""
    visualize_image("gradient", image_path)


@app.command()
def hog(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize Histogram of Oriented Gradients (HoG)."""
    visualize_image("hog", image_path)


@app.command()
def keypoint(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize keypoints."""
    visualize_image("keypoint", image_path)


@app.command()
def lbp(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize Local Binary Patterns (LBP)."""
    visualize_image("lbp", image_path)


@app.command()
def power_spectrum(
    image_path: Annotated[str, typer.Argument(help="Path to the input image")],
) -> None:
    """Visualize power spectrum."""
    visualize_image("power_spectrum", image_path)

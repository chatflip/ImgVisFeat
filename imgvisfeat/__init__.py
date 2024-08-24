from importlib.metadata import version

from .Visualizer import Visualizer  # noqa: F401

__all__ = ["Visualizer"]

__version__ = version("imgvisfeat")

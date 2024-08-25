from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

__all__ = [
    "ColorChannelResult",
    "GradientResult",
    "PowerSpectrumResult",
    "HogResult",
    "LBPResult",
    "KeypointResult",
]


class VisualizationResult:
    """Base class for visualization results."""

    pass


@dataclass
class ColorChannelResult(VisualizationResult):
    """A dataclass for storing color channel results."""

    blue: NDArray[np.uint8]
    green: NDArray[np.uint8]
    red: NDArray[np.uint8]


@dataclass
class GradientResult(VisualizationResult):
    """A dataclass for storing gradient results."""

    gradient_x: NDArray[np.uint8]
    gradient_y: NDArray[np.uint8]
    gradient_xy: NDArray[np.uint8]


@dataclass
class PowerSpectrumResult(VisualizationResult):
    """A dataclass for storing power spectrum results."""

    power_spectrum: NDArray[np.uint8]


@dataclass
class HogResult(VisualizationResult):
    """A dataclass for storing Histogram of Oriented Gradient results."""

    hog: NDArray[np.uint8]


@dataclass
class LBPResult(VisualizationResult):
    """A dataclass for storing Local Binary Pattern results."""

    lbp: NDArray[np.uint8]


@dataclass
class KeypointResult(VisualizationResult):
    """A dataclass for storing keypoint results."""

    keypoint: NDArray[np.uint8]
    rich_keypoint: NDArray[np.uint8]

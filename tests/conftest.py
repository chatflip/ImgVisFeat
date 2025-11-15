import numpy as np
import pytest
from numpy.typing import NDArray

import imfv

from .utils import get_image


@pytest.fixture(name="color_image")
def color_image() -> NDArray[np.uint8]:
    """Return a color image.

    Returns:
        NDArray[np.uint8]: Color image.
    """
    return get_image(is_gray=False)


@pytest.fixture(name="gray_image")
def gray_image() -> NDArray[np.uint8]:
    """Return a grayscale image.

    Returns:
        NDArray[np.uint8]: Grayscale image.
    """
    return get_image(is_gray=True)


@pytest.fixture(name="color_channel_visualizer")
def color_channel_visualizer() -> imfv.ColorChannelVisualizer:
    """Fixture to create a ColorChannelVisualizer instance."""
    return imfv.ColorChannelVisualizer()


@pytest.fixture(name="gray_gradient_visualizer")
def gray_gradient_visualizer() -> imfv.GrayGradientVisualizer:
    """Fixture to create a GrayGradientVisualizer instance."""
    return imfv.GrayGradientVisualizer()


@pytest.fixture(name="color_gradient_visualizer")
def color_gradient_visualizer() -> imfv.ColorGradientVisualizer:
    """Fixture to create a ColorGradientVisualizer instance."""
    return imfv.ColorGradientVisualizer()


@pytest.fixture(name="hog_visualizer")
def hog_visualizer() -> imfv.HoGVisualizer:
    """Fixture to create a HoGVisualizer instance."""
    return imfv.HoGVisualizer()


@pytest.fixture(name="lbp_visualizer")
def lbp_visualizer() -> imfv.LBPVisualizer:
    """Fixture to create a LBPVisualizer instance."""
    return imfv.LBPVisualizer()


@pytest.fixture(name="power_spectrum_visualizer")
def power_spectrum_visualizer() -> imfv.PowerSpectrumVisualizer:
    """Fixture to create a PowerSpectrumVisualizer instance."""
    return imfv.PowerSpectrumVisualizer()

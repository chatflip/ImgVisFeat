import numpy as np
import pytest
from numpy.typing import NDArray

import imvf

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
def color_channel_visualizer() -> imvf.ColorChannelVisualizer:
    """Fixture to create a ColorChannelVisualizer instance."""
    return imvf.ColorChannelVisualizer()


@pytest.fixture(name="gray_gradient_visualizer")
def gray_gradient_visualizer() -> imvf.GrayGradientVisualizer:
    """Fixture to create a GrayGradientVisualizer instance."""
    return imvf.GrayGradientVisualizer()


@pytest.fixture(name="color_gradient_visualizer")
def color_gradient_visualizer() -> imvf.ColorGradientVisualizer:
    """Fixture to create a ColorGradientVisualizer instance."""
    return imvf.ColorGradientVisualizer()


@pytest.fixture(name="hog_visualizer")
def hog_visualizer() -> imvf.HoGVisualizer:
    """Fixture to create a HoGVisualizer instance."""
    return imvf.HoGVisualizer()


@pytest.fixture(name="lbp_visualizer")
def lbp_visualizer() -> imvf.LBPVisualizer:
    """Fixture to create a LBPVisualizer instance."""
    return imvf.LBPVisualizer()


@pytest.fixture(name="power_spectrum_visualizer")
def power_spectrum_visualizer() -> imvf.PowerSpectrumVisualizer:
    """Fixture to create a PowerSpectrumVisualizer instance."""
    return imvf.PowerSpectrumVisualizer()

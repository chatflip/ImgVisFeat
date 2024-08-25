import numpy as np
import pytest
from numpy.typing import NDArray

import imgvisfeat as ivf

from .utils import get_image


@pytest.fixture
def color_image() -> NDArray[np.uint8]:
    """Return a color image.

    Returns:
        NDArray[np.uint8]: Color image.
    """
    return get_image(is_gray=False)


@pytest.fixture
def gray_image() -> NDArray[np.uint8]:
    """Return a grayscale image.

    Returns:
        NDArray[np.uint8]: Grayscale image.
    """
    return get_image(is_gray=True)


@pytest.fixture
def color_channel_visualizer() -> ivf.ColorChannelVisualizer:
    """Fixture to create a ColorChannelVisualizer instance."""
    return ivf.ColorChannelVisualizer()


@pytest.fixture
def gray_gradient_visualizer() -> ivf.GrayGradientVisualizer:
    """Fixture to create a GrayGradientVisualizer instance."""
    return ivf.GrayGradientVisualizer()


@pytest.fixture
def color_gradient_visualizer() -> ivf.ColorGradientVisualizer:
    """Fixture to create a ColorGradientVisualizer instance."""
    return ivf.ColorGradientVisualizer()


@pytest.fixture
def hog_visualizer() -> ivf.HoGVisualizer:
    """Fixture to create a HoGVisualizer instance."""
    return ivf.HoGVisualizer()


@pytest.fixture
def akaze_visualizer() -> ivf.KeypointVisualizer:
    """Fixture to create a AKAZEVisualizer instance."""
    return ivf.KeypointVisualizer("AKAZE")


@pytest.fixture
def orb_visualizer() -> ivf.KeypointVisualizer:
    """Fixture to create a ORBVisualizer instance."""
    return ivf.KeypointVisualizer("ORB")


@pytest.fixture
def sift_visualizer() -> ivf.KeypointVisualizer:
    """Fixture to create a SIFTVisualizer instance."""
    return ivf.KeypointVisualizer("SIFT")


@pytest.fixture
def lbp_visualizer() -> ivf.LBPVisualizer:
    """Fixture to create a LBPVisualizer instance."""
    return ivf.LBPVisualizer()


@pytest.fixture
def abstract_visualizer() -> ivf.AbstractVisualizer:
    """Fixture to create a AbstractVisualizer instance."""
    return ivf.AbstractVisualizer()


@pytest.fixture
def power_spectrum_visualizer() -> ivf.PowerSpectrumVisualizer:
    """Fixture to create a PowerSpectrumVisualizer instance."""
    return ivf.PowerSpectrumVisualizer()

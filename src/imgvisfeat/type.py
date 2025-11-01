from typing import Any

import numpy as np
from numpy.typing import NDArray
from pydantic import BaseModel, ConfigDict, field_validator

__all__ = [
    "ColorChannelResult",
    "GradientResult",
    "PowerSpectrumResult",
    "HogResult",
    "LBPResult",
    "KeypointResult",
]


class VisualizationResult(BaseModel):
    """Base class for visualization results.

    This class provides common functionality for all visualization results,
    including validation and immutability.
    """

    model_config = ConfigDict(
        frozen=True,  # Make instances immutable
        arbitrary_types_allowed=True,  # Allow NumPy arrays
    )

    @field_validator("*", mode="before")
    @classmethod
    def validate_numpy_array(cls, v: Any) -> Any:
        """Validate that the value is a NumPy array with correct dtype.

        Args:
            v: The value to validate.

        Returns:
            The validated NumPy array.

        Raises:
            ValueError: If the value is not a valid NumPy array or has incorrect dtype.
        """
        if not isinstance(v, np.ndarray):
            raise ValueError(f"Expected numpy.ndarray, got {type(v)}")

        if v.dtype != np.uint8:
            raise ValueError(f"Expected dtype uint8, got {v.dtype}")

        if v.ndim not in (2, 3):
            raise ValueError(f"Expected 2D or 3D array, got {v.ndim}D array")

        return v


class ColorChannelResult(VisualizationResult):
    """A Pydantic model for storing color channel results.

    Attributes:
        blue: Blue channel as uint8 array.
        green: Green channel as uint8 array.
        red: Red channel as uint8 array.
    """

    blue: NDArray[np.uint8]
    green: NDArray[np.uint8]
    red: NDArray[np.uint8]


class GradientResult(VisualizationResult):
    """A Pydantic model for storing gradient results.

    Attributes:
        gradient_x: Gradient in x direction as uint8 array.
        gradient_y: Gradient in y direction as uint8 array.
        gradient_xy: Gradient in xy direction as uint8 array.
    """

    gradient_x: NDArray[np.uint8]
    gradient_y: NDArray[np.uint8]
    gradient_xy: NDArray[np.uint8]


class PowerSpectrumResult(VisualizationResult):
    """A Pydantic model for storing power spectrum results.

    Attributes:
        power_spectrum: Power spectrum as uint8 array.
    """

    power_spectrum: NDArray[np.uint8]


class HogResult(VisualizationResult):
    """A Pydantic model for storing Histogram of Oriented Gradient results.

    Attributes:
        hog: HoG features as uint8 array.
    """

    hog: NDArray[np.uint8]


class LBPResult(VisualizationResult):
    """A Pydantic model for storing Local Binary Pattern results.

    Attributes:
        lbp: LBP features as uint8 array.
    """

    lbp: NDArray[np.uint8]


class KeypointResult(VisualizationResult):
    """A Pydantic model for storing keypoint results.

    Attributes:
        keypoint: Keypoint positions as uint8 array.
        rich_keypoint: Rich keypoint visualization as uint8 array.
    """

    keypoint: NDArray[np.uint8]
    rich_keypoint: NDArray[np.uint8]

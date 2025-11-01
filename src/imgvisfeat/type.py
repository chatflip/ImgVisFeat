from typing import Any, TypeAlias

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

ImageArray: TypeAlias = NDArray[np.uint8]


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
    def _validate_numpy_array(cls, v: Any) -> ImageArray:
        """Validate NumPy array with uint8 dtype and 2D/3D shape.

        Args:
            v: The value to validate.

        Returns:
            The validated NumPy array with dtype uint8.

        Raises:
            ValueError: If validation fails.
        """
        if not isinstance(v, np.ndarray):
            raise ValueError(f"Expected numpy.ndarray, got {type(v).__name__}")

        if v.dtype != np.uint8:
            raise ValueError(f"Expected dtype uint8, got {v.dtype}")

        if v.ndim not in (2, 3):
            raise ValueError(f"Expected 2D or 3D array, got {v.ndim}D")

        return v


class ColorChannelResult(VisualizationResult):
    """A Pydantic model for storing color channel results.

    Attributes:
        blue: Blue channel as uint8 array.
        green: Green channel as uint8 array.
        red: Red channel as uint8 array.
    """

    blue: ImageArray
    green: ImageArray
    red: ImageArray


class GradientResult(VisualizationResult):
    """A Pydantic model for storing gradient results.

    Attributes:
        gradient_x: Gradient in x direction as uint8 array.
        gradient_y: Gradient in y direction as uint8 array.
        gradient_xy: Gradient in xy direction as uint8 array.
    """

    gradient_x: ImageArray
    gradient_y: ImageArray
    gradient_xy: ImageArray


class PowerSpectrumResult(VisualizationResult):
    """A Pydantic model for storing power spectrum results.

    Attributes:
        power_spectrum: Power spectrum as uint8 array.
    """

    power_spectrum: ImageArray


class HogResult(VisualizationResult):
    """A Pydantic model for storing Histogram of Oriented Gradient results.

    Attributes:
        hog: HoG features as uint8 array.
    """

    hog: ImageArray


class LBPResult(VisualizationResult):
    """A Pydantic model for storing Local Binary Pattern results.

    Attributes:
        lbp: LBP features as uint8 array.
    """

    lbp: ImageArray


class KeypointResult(VisualizationResult):
    """A Pydantic model for storing keypoint results.

    Attributes:
        keypoint: Keypoint positions as uint8 array.
        rich_keypoint: Rich keypoint visualization as uint8 array.
    """

    keypoint: ImageArray
    rich_keypoint: ImageArray

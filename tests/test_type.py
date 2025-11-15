import numpy as np
import pytest
from pydantic import ValidationError

from ivf.type import ColorChannelResult


def test_color_channel_result_validation_not_ndarray() -> None:
    """Test ColorChannelResult validation with non-ndarray input."""
    valid_array = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises(ValidationError) as exc_info:
        ColorChannelResult(blue=valid_array, green=valid_array, red=[1, 2, 3])  # type: ignore[arg-type]
    assert "Expected numpy.ndarray, got list" in str(exc_info.value)


def test_color_channel_result_validation_wrong_dtype() -> None:
    """Test ColorChannelResult validation with wrong dtype."""
    valid_array = np.zeros((10, 10, 3), dtype=np.uint8)
    invalid_array = np.zeros((10, 10, 3), dtype=np.float32)
    with pytest.raises(ValidationError) as exc_info:
        ColorChannelResult(blue=valid_array, green=valid_array, red=invalid_array)  # type: ignore[arg-type]
    assert "Expected dtype uint8, got float32" in str(exc_info.value)


def test_color_channel_result_validation_wrong_ndim() -> None:
    """Test ColorChannelResult validation with wrong ndim."""
    valid_array = np.zeros((10, 10, 3), dtype=np.uint8)
    invalid_array = np.zeros((10,), dtype=np.uint8)  # 1D array
    with pytest.raises(ValidationError) as exc_info:
        ColorChannelResult(blue=valid_array, green=valid_array, red=invalid_array)
    assert "Expected 2D or 3D array, got 1D" in str(exc_info.value)

from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import NDArray

from .type import VisualizationResult


class AbstractVisualizer(ABC):
    """Abstract base class for image visualizers."""

    @abstractmethod
    def __call__(self, source: NDArray[np.uint8]) -> VisualizationResult:
        """Apply visualization to the source image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            VisualizationResult: The result of the visualization.
        """
        pass  # pragma: no cover

    def __str__(self) -> str:
        """Return the name of the visualizer.

        Returns:
            str: The name of the visualizer.
        """
        return self.__class__.__name__

import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import LBPResult


class LBPVisualizer(AbstractVisualizer):
    """A class for computing the Local Binary Pattern (LBP) of an image."""

    def __init__(self) -> None:
        """Initialize the LBPVisualizer class."""
        pass

    def __call__(self, source: NDArray[np.uint8]) -> LBPResult:
        """Compute the Local Binary Pattern (LBP) of an image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            LBPResult: The LBP image.
        """
        if source.ndim != 2:
            gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        else:
            gray = source.copy()
        counter = 0
        lbp = 8 * [0]
        lbp_image = np.zeros((gray.shape[0] - 2, gray.shape[1] - 2), dtype=np.uint8)
        for centerY in range(1, gray.shape[0] - 1):
            for centerX in range(1, gray.shape[1] - 1):
                for yy in range(centerY - 1, centerY + 2):
                    for xx in range(centerX - 1, centerX + 2):
                        if (xx != centerX) or (yy != centerY):
                            if gray[centerY, centerX] >= gray[yy, xx]:
                                lbp[counter] = 0
                            else:
                                lbp[counter] = 1
                            counter += 1
                lbp_pix = (
                    lbp[0] * 2**7
                    + lbp[1] * 2**6
                    + lbp[2] * 2**5
                    + lbp[4] * 2**4
                    + lbp[7] * 2**3
                    + lbp[6] * 2**2
                    + lbp[5] * 2**1
                    + lbp[3] * 2**0
                )
                lbp_image[centerY - 1, centerX - 1] = lbp_pix
                counter = 0
        lbp_image = cv2.copyMakeBorder(  # type: ignore
            lbp_image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0
        )
        return LBPResult(lbp=lbp_image)

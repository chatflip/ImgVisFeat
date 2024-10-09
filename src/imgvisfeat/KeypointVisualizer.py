import cv2
import numpy as np
from numpy.typing import NDArray

from .AbstractVisualizer import AbstractVisualizer
from .type import KeypointResult


class KeypointVisualizer(AbstractVisualizer):
    """A class for visualizing keypoints in an image."""

    def __init__(self, algorithm_name: str) -> None:
        """Initialize the KeypointVisualizer class."""
        if algorithm_name not in ["AKAZE", "SIFT", "ORB"]:
            raise ValueError(
                "Invalid algorithm name. Choose from 'AKAZE', 'SIFT', or 'ORB'."
            )
        self.algorithm_name = algorithm_name

    def __call__(self, source: NDArray[np.uint8]) -> KeypointResult:
        """Visualize keypoints in an image.

        Args:
            source (NDArray[np.uint8]): The source image.

        Returns:
            KeyPointResult: The image with keypoints and the image with rich keypoints.
        """
        color = source.copy()
        if source.ndim != 3:
            color = cv2.cvtColor(source, cv2.COLOR_GRAY2BGR).astype(np.uint8)
        if self.algorithm_name == "AKAZE":
            kp_image, rich_image = self.make_akaze_image(color)
        elif self.algorithm_name == "SIFT":
            kp_image, rich_image = self.make_sift_image(color)
        elif self.algorithm_name == "ORB":
            kp_image, rich_image = self.make_orb_image(color)
        else:
            raise ValueError(f"Invalid algorithm name: {self.algorithm_name}")
        return KeypointResult(kp_image, rich_image)

    def make_akaze_image(
        self, color: NDArray[np.uint8]
    ) -> tuple[NDArray[np.uint8], NDArray[np.uint8]]:
        """Create an image with keypoints using the AKAZE algorithm.

        Args:
            color (NDArray[np.uint8]): The source image.

        Returns:
            tuple[NDArray[np.uint8], NDArray[np.uint8]]:
                The image with keypoints and the image with rich keypoints.
        """
        gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        kp_image = color.copy()
        rich_image = color.copy()
        detector = cv2.AKAZE_create()  # type: ignore
        keypoints = detector.detect(gray)
        circle_color = (255, 255, 0)
        for key in keypoints:
            cv2.circle(
                kp_image,
                (np.uint64(key.pt[0]), np.uint64(key.pt[1])),  # type: ignore
                3,
                circle_color,
                1,
            )
        cv2.drawKeypoints(
            rich_image,
            keypoints,
            rich_image,
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )
        print(f"Number of keypoints (AKAZE): {len(keypoints)}")
        return kp_image, rich_image

    def make_sift_image(
        self, color: NDArray[np.uint8]
    ) -> tuple[NDArray[np.uint8], NDArray[np.uint8]]:
        """Create an image with keypoints using the SIFT algorithm.

        Args:
            color (NDArray[np.uint8]): The source image.

        Returns:
            tuple[NDArray[np.uint8], NDArray[np.uint8]]:
                The image with keypoints and the image with rich keypoints.
        """
        gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        kp_image = color.copy()
        rich_image = color.copy()
        detector = cv2.SIFT_create()  # type: ignore
        keypoints = detector.detect(gray)
        circle_color = (255, 255, 0)
        for key in keypoints:
            cv2.circle(
                kp_image,
                (np.uint64(key.pt[0]), np.uint64(key.pt[1])),  # type: ignore
                3,
                circle_color,
                1,
            )
        cv2.drawKeypoints(
            rich_image,
            keypoints,
            rich_image,
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )
        print(f"Number of keypoints (SIFT) : {len(keypoints)}")
        return kp_image, rich_image

    def make_orb_image(
        self, color: NDArray[np.uint8]
    ) -> tuple[NDArray[np.uint8], NDArray[np.uint8]]:
        """Create an image with keypoints using the ORB algorithm.

        Args:
            color (NDArray[np.uint8]): The source image.

        Returns:
            tuple[NDArray[np.uint8], NDArray[np.uint8]]:
                The image with keypoints and the image with rich keypoints.
        """
        gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        kp_image = color.copy()
        rich_image = color.copy()
        detector = cv2.ORB_create()  # type: ignore
        keypoints = detector.detect(gray)
        circle_color = (255, 255, 0)
        cv2.drawKeypoints(kp_image, keypoints, kp_image, color=circle_color)
        cv2.drawKeypoints(
            rich_image,
            keypoints,
            rich_image,
            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )
        print(f"Number of keypoints (ORB): {len(keypoints)}")
        return kp_image, rich_image

    def __str__(self) -> str:
        """Return the name of the visualizer.

        Returns:
            str: The name of the visualizer.
        """
        return f"{self.__class__.__name__}({self.algorithm_name})"

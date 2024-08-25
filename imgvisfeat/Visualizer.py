"""Module for image visualization in the ImgVisFeat package.

This module contains the Visualizer class, which provides functionality
for loading, processing, and displaying or saving visualized images.
It supports various visualization parameters and options to enhance
image representation for analysis and presentation purposes.

Classes:
    Visualizer: Main class for image visualization operations.
"""

from __future__ import annotations

import os

import cv2


class Visualizer:
    """A class for visualizing images.

    This class provides functionality to visualize images, with options
    to display them on screen or save them to a specified directory.

    Attributes:
        params (dict): Additional parameters for visualization.

    Example:
        >>> vis = Visualizer()
        >>> vis.visualize('path/to/image.jpg', dst_root='output_folder')
    """

    def __init__(self, **params: dict) -> None:
        """Initialize the Visualizer.

        Args:
            **params: Additional parameters for visualization.
                      These can include color maps, scaling factors, etc.
        """
        self.params = params

    def visualize(self, src_image_path: str, dst_root: str | None = None) -> None:
        """Visualize the image.

        This method loads an image from the given path, applies any
        visualization parameters, and either displays the image or
        saves it to the specified destination.

        Args:
            src_image_path (str): Path to the source image file.
            dst_root (str | None, optional): Root directory to save the
                visualized image. If None, the image is displayed on screen.
                Defaults to None.

        Raises:
            ValueError: If the src_image_path is invalid or the image
                        cannot be loaded.

        Example:
            >>> visualizer = Visualizer()
            >>> visualizer.visualize('input.jpg', dst_root='output')
        """
        self.check_image_assertions(src_image_path)
        image = cv2.imread(src_image_path)
        if dst_root is None:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            os.makedirs(dst_root, exist_ok=True)
            dst_image_path = os.path.join(dst_root, os.path.basename(src_image_path))
            cv2.imwrite(dst_image_path, image)

    def check_image_assertions(self, src_image_path: str) -> None:
        """Check if the image path is valid.

        Args:
            src_image_path (str): Path to the image.

        Raises:
            ValueError: If the image is not found.
            ValueError: If the image path is not a file.
            ValueError: If the image path is not a image.
        """
        if not os.path.exists(src_image_path):
            raise ValueError(f"Image not found: {src_image_path}")
        elif not os.path.isfile(src_image_path):
            raise ValueError(f"Image path must be a file, but got {src_image_path}")
        try:
            image = cv2.imread(src_image_path)
            _ = image.shape
        except AttributeError:
            raise ValueError(f"Image not found: {src_image_path}")

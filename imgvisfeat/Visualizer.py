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

from .ColorChannelVisualizer import ColorChannelVisualizer
from .GradientVisualizer import ColorGradientVisualizer, GrayGradientVisualizer
from .HoGVisualizer import HoGVisualizer
from .KeypointVisualizer import KeypointVisualizer
from .LBPVisualizer import LBPVisualizer
from .PowerSpectrumVisualizer import PowerSpectrumVisualizer


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
        self.color_channel_visualizer = ColorChannelVisualizer()
        self.hog_visualizer = HoGVisualizer()
        self.power_spectrum_visualizer = PowerSpectrumVisualizer()
        self.sift_visualizer = KeypointVisualizer("SIFT")
        self.akaze_visualizer = KeypointVisualizer("AKAZE")
        self.orb_visualizer = KeypointVisualizer("ORB")
        self.color_gradient_visualizer = ColorGradientVisualizer()
        self.gray_gradient_visualizer = GrayGradientVisualizer()
        self.lbp_visualizer = LBPVisualizer()

    def visualize(self, src_image_path: str) -> None:
        """Visualize the image.

        This method loads an image from the given path, applies any
        visualization parameters, and either displays the image or
        saves it to the specified destination.

        Args:
            src_image_path (str): Path to the source image file.

        Raises:
            ValueError: If the src_image_path is invalid or the image
                        cannot be loaded.

        Example:
            >>> visualizer = Visualizer()
            >>> visualizer.visualize('input.jpg', dst_root='output')
        """
        print(f"Visualizing {src_image_path}")
        self.check_image_assertions(src_image_path)
        name, _ = os.path.splitext(os.path.basename(src_image_path))
        image = cv2.imread(src_image_path).astype("uint8")
        color_channel_result = self.color_channel_visualizer(image)
        gradient_result = self.color_gradient_visualizer(image)
        gray_gradient_result = self.gray_gradient_visualizer(image)
        hog_result = self.hog_visualizer(image)
        power_spectrum_result = self.power_spectrum_visualizer(image)
        sift_result = self.sift_visualizer(image)
        akaze_result = self.akaze_visualizer(image)
        orb_result = self.orb_visualizer(image)
        lbp_result = self.lbp_visualizer(image)

        os.makedirs(name, exist_ok=True)
        dst_path = os.path.join(name, "%s.png")
        cv2.imwrite(dst_path % "original", image)
        cv2.imwrite(dst_path % "channel_blue", color_channel_result.blue)
        cv2.imwrite(dst_path % "channel_green", color_channel_result.green)
        cv2.imwrite(dst_path % "channel_red", color_channel_result.red)
        cv2.imwrite(dst_path % "color_gradient_x", gradient_result.gradient_x)
        cv2.imwrite(dst_path % "color_gradient_y", gradient_result.gradient_y)
        cv2.imwrite(dst_path % "color_gradient_xy", gradient_result.gradient_xy)
        cv2.imwrite(dst_path % "gray_gradient_x", gray_gradient_result.gradient_x)
        cv2.imwrite(dst_path % "gray_gradient_y", gray_gradient_result.gradient_y)
        cv2.imwrite(dst_path % "gray_gradient_xy", gray_gradient_result.gradient_xy)
        cv2.imwrite(dst_path % "hog", hog_result.hog)
        cv2.imwrite(dst_path % "power_spectrum", power_spectrum_result.power_spectrum)
        cv2.imwrite(dst_path % "keypoint_sift_position", sift_result.keypoint)
        cv2.imwrite(dst_path % "keypoint_sift_rich", sift_result.rich_keypoint)
        cv2.imwrite(dst_path % "keypoint_akaze_position", akaze_result.keypoint)
        cv2.imwrite(dst_path % "keypoint_akaze_rich", akaze_result.rich_keypoint)
        cv2.imwrite(dst_path % "keypoint_orb_position", orb_result.keypoint)
        cv2.imwrite(dst_path % "keypoint_orb_rich", orb_result.rich_keypoint)
        cv2.imwrite(dst_path % "lbp", lbp_result.lbp)

        cv2.imshow("Original", image)
        cv2.imshow("Blue Channel", color_channel_result.blue)
        cv2.imshow("Green Channel", color_channel_result.green)
        cv2.imshow("Red Channel", color_channel_result.red)
        cv2.imshow("Color Gradient X", gradient_result.gradient_x)
        cv2.imshow("Color Gradient Y", gradient_result.gradient_y)
        cv2.imshow("Color Gradient X and Y", gradient_result.gradient_xy)
        cv2.imshow("Gray Gradient X", gray_gradient_result.gradient_x)
        cv2.imshow("Gray Gradient Y", gray_gradient_result.gradient_y)
        cv2.imshow("Gray Gradient X and Y", gray_gradient_result.gradient_xy)
        cv2.imshow("HoG", hog_result.hog)
        cv2.imshow("Power Spectrum", power_spectrum_result.power_spectrum)
        cv2.imshow("SIFT keypoint", sift_result.keypoint)
        cv2.imshow("SIFT rich keypoint", sift_result.rich_keypoint)
        cv2.imshow("AKAZE keypoint", akaze_result.keypoint)
        cv2.imshow("AKAZE rich keypoint", akaze_result.rich_keypoint)
        cv2.imshow("ORB keypoint", orb_result.keypoint)
        cv2.imshow("ORB rich keypoint", orb_result.rich_keypoint)
        cv2.imshow("LBP", lbp_result.lbp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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
            raise FileNotFoundError(f"Image not found: {src_image_path}")
        elif not os.path.isfile(src_image_path):
            raise IsADirectoryError(
                f"Image path must be a file, but got {src_image_path}"
            )
        try:
            image = cv2.imread(src_image_path)
            _ = image.shape
        except AttributeError:
            raise ValueError(f"Image not found: {src_image_path}")

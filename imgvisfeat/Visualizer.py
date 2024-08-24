from __future__ import annotations

import os

import cv2


class Visualizer:
    def __init__(self, **params: dict) -> None:
        self.params = params

    def visualize(self, src_image_path: str, dst_root: str | None = None) -> None:
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


if __name__ == "__main__":
    visualizer = Visualizer()
    visualizer.visualize("tests/resources/images/test_image.jpg")

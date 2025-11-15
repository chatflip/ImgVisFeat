import argparse
import sys

import imvf


def main() -> None:
    """Main entry point for the ImgVisFeat CLI.

    This function parses command-line arguments, calls the appropriate
    visualization method, and either displays or saves the result.
    """
    parser = argparse.ArgumentParser(description="ImgVisFeat: Visualize image features")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument(
        "--method",
        type=str,
        default="all",
        choices=[
            "all",
            "color_channel",
            "gradient",
            "hog",
            "keypoint",
            "lbp",
            "power_spectrum",
        ],
        help="Visualization method to use",
    )

    args = parser.parse_args()

    visualizer = imvf.Visualizer()
    try:
        visualizer.visualize(args.image_path)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        print("Visualization failed.")
        sys.exit(1)
    print("Visualization complete.")
    sys.exit(0)

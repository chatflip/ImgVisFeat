# ImgVisFeat

|             |                                                                                                                                                                                                                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project     | [![PyPI version](https://badge.fury.io/py/ImgVisFeat.svg)](https://pypi.org/project/ImgVisFeat/) [![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://chatflip.github.io/ImgVisFeat/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) |
| Package     | [![Python Versions](https://img.shields.io/pypi/pyversions/ImgVisFeat.svg)](https://pypi.org/project/ImgVisFeat/)                                                                                                                                                                                                          |
| Development | [![Build Status](https://github.com/chatflip/ImgVisFeat/actions/workflows/lints_tests.yml/badge.svg)](https://github.com/chatflip/ImgVisFeat/actions) [![Codecov](https://codecov.io/gh/chatflip/ImgVisFeat/branch/main/graph/badge.svg)](https://codecov.io/gh/chatflip/ImgVisFeat)                                       |
| Community   | [![GitHub issues](https://img.shields.io/github/issues/chatflip/ImgVisFeat.svg)](https://github.com/chatflip/ImgVisFeat/issues) [![GitHub stars](https://img.shields.io/github/stars/chatflip/ImgVisFeat.svg)](https://github.com/chatflip/ImgVisFeat/stargazers)                                                          |

ImgVisFeat is a Python library for image visualization and feature extraction, providing a comprehensive set of tools for analyzing and visualizing various image features.

## Features

ImgVisFeat provides the following visualization and feature extraction capabilities:

- **Color Channel Visualization**: Extract and visualize individual RGB color channels
- **Gradient Visualization**: Compute and visualize image gradients in X, Y, and combined XY directions
  - ColorGradientVisualizer: For color images
  - GrayGradientVisualizer: For grayscale images
- **HoG (Histogram of Oriented Gradients)**: Visualize feature descriptors for object detection
- **LBP (Local Binary Patterns)**: Extract texture descriptors for texture classification
- **Keypoint Detection**: Detect and visualize keypoints using SIFT, AKAZE, or ORB algorithms
- **Power Spectrum Analysis**: Analyze frequency domain characteristics of images
- **CLI Tool**: Command-line interface for quick visualizations

## Requirements

- Python >= 3.10

## Installation

### Install from PyPI

```bash
# Using pip
pip install ImgVisFeat

# Using uv (faster alternative)
uv add ImgVisFeat
```

### Development Installation

For development, we recommend using [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/chatflip/ImgVisFeat.git
cd ImgVisFeat
uv sync

# Install pre-commit hooks
pre-commit install
```

## Development

This project uses `make` commands for common development tasks:

```bash
# Show available commands
make help

# Run tests
make test

# Format code
make format

# Run linting
make lint

# Build documentation
make builddocs
```

For more details on development workflows, see [CLAUDE.md](CLAUDE.md).

### Verify Installation

```python
import ivf
print(ivf.__version__)
```

## Quick Start

### Using the All-in-One Visualizer

The `Visualizer` class provides a convenient way to apply all visualization methods at once:

```python
import ivf

# Create visualizer instance
visualizer = ivf.Visualizer()

# Visualize all features and save results to a directory named after the image
visualizer.visualize("path/to/image.jpg")
```

This will display all visualizations in OpenCV windows and save the results to a directory named `path/to/image/`.

### Using Individual Visualizers

You can also use individual visualizers for specific analyses:

```python
import cv2
import ivf

# Load image
image = cv2.imread("path/to/image.jpg")

# Color channel visualization
color_channel = ivf.ColorChannelVisualizer()
result = color_channel(image)
cv2.imshow("Blue Channel", result.blue)
cv2.imshow("Green Channel", result.green)
cv2.imshow("Red Channel", result.red)

# Gradient visualization (for color images)
gradient = ivf.ColorGradientVisualizer()
result = gradient(image)
cv2.imshow("Gradient X", result.gradient_x)
cv2.imshow("Gradient Y", result.gradient_y)
cv2.imshow("Gradient XY", result.gradient_xy)

# HoG visualization
hog = ivf.HoGVisualizer()
result = hog(image)
cv2.imshow("HoG", result.hog)

# Keypoint detection
keypoint = ivf.KeypointVisualizer(algorithm="SIFT")  # or "AKAZE", "ORB"
result = keypoint(image)
cv2.imshow("Keypoints", result.keypoint)
cv2.imshow("Rich Keypoints", result.rich_keypoint)
```

### Using the CLI

ImgVisFeat provides a command-line interface for quick visualizations:

```bash
# Visualize all features
ivf path/to/image.jpg

# Visualize specific feature (currently all methods are applied)
ivf path/to/image.jpg --method all
```

Available methods:

- `all`: All visualization methods (default)
- `color_channel`: Color channel visualization
- `gradient`: Gradient visualization
- `hog`: HoG visualization
- `lbp`: LBP visualization
- `keypoint`: Keypoint detection
- `power_spectrum`: Power spectrum analysis

## Documentation

For full documentation, including API reference and tutorials, please visit our [documentation site](https://chatflip.github.io/ImgVisFeat/).

## Project Status

ImgVisFeat is a personal project created for learning and experimentation. While it's open-source and you're welcome to use and learn from it, please note that it may not be actively maintained or updated regularly.

## Feedback and Questions

This is a practice repository, but I'm always eager to learn. If you have any questions about the project or suggestions for improvement, feel free to [open an issue](https://github.com/chatflip/ImgVisFeat/issues) for discussion. Please understand that responses may not be immediate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[chatflip](https://github.com/chatflip)

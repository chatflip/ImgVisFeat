# ImgVisFeat

|             |                                                                                                                                                                                                                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project     | [![PyPI version](https://badge.fury.io/py/ImgVisFeat.svg)](https://pypi.org/project/ImgVisFeat/) [![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://chatflip.github.io/ImgVisFeat/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) |
| Package     | [![Python Versions](https://img.shields.io/pypi/pyversions/ImgVisFeat.svg)](https://pypi.org/project/ImgVisFeat/)                                                                                                                                                                                                          |
| Development | [![Build Status](https://github.com/chatflip/ImgVisFeat/actions/workflows/lints_tests.yml/badge.svg)](https://github.com/chatflip/ImgVisFeat/actions) [![Codecov](https://codecov.io/gh/chatflip/ImgVisFeat/branch/main/graph/badge.svg)](https://codecov.io/gh/chatflip/ImgVisFeat)                                       |
| Community   | [![GitHub issues](https://img.shields.io/github/issues/chatflip/ImgVisFeat.svg)](https://github.com/chatflip/ImgVisFeat/issues) [![GitHub stars](https://img.shields.io/github/stars/chatflip/ImgVisFeat.svg)](https://github.com/chatflip/ImgVisFeat/stargazers)                                                          |

ImgVisFeat is a powerful Python library for image visualization and feature extraction, designed to simplify and enhance your computer vision workflows.

## Features

- Fast and efficient image processing algorithms
- Comprehensive set of feature extraction techniques
- Easy-to-use visualization tools
- Seamless integration with popular CV libraries
- Extensive documentation and examples

## Requirements

- Python >= 3.10
- NumPy < 2.0.0
- OpenCV Python
- scikit-image

## Installation

### Install from PyPI (Recommended)

Using pip:

```bash
pip install ImgVisFeat
```

Using poetry:

```bash
poetry add ImgVisFeat
```

### Install from Source

Clone the repository and install with pip:

```bash
git clone https://github.com/chatflip/ImgVisFeat.git
cd ImgVisFeat
pip install .
```

Or with poetry:

```bash
git clone https://github.com/chatflip/ImgVisFeat.git
cd ImgVisFeat
poetry install
```

### Install Specific Version

Using pip:

```bash
# Install from a specific commit
pip install git+https://github.com/chatflip/ImgVisFeat.git@10fb495

# Install from a specific tag/release
pip install git+https://github.com/chatflip/ImgVisFeat.git@v0.1.0
```

Using poetry:

```bash
# Install from a specific commit
poetry add git+https://github.com/chatflip/ImgVisFeat.git#10fb495

# Install from a specific tag/release
poetry add git+https://github.com/chatflip/ImgVisFeat.git#v0.1.0
```

### Development Installation

For contributing or development:

```bash
git clone https://github.com/chatflip/ImgVisFeat.git
cd ImgVisFeat
uv sync --all-extras

# Install pre-commit hooks
pre-commit install
```

### Verify Installation

```python
import imgvisfeat as ivf
print(ivf.__version__)
```

## Quick Start

```python
import cv2
import imgvisfeat as ivf

visualizer = ivf.Visualizer()

# Show Result and Save Result to "path/to/image" Directory 
visualizer.visualize("path/to/image.jpg")

# Return Result as image
image = cv2.imread("path/to/image.jpg")
color_gradient_visualizer = ivf.ColorGradientVisualizer()
result = color_gradient_visualizer.visualize(image)
cv2.imshow("Color Gradient X Direction", result.gradient_x)
cv2.imshow("Color Gradient X and Y Direction", result.gradient_xy)
```

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

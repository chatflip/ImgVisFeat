# Getting Started

This guide will help you install and start using ImgVisFeat.

## Installation

### Requirements

- Python >= 3.10

### Install from PyPI

Install ImgVisFeat using pip:

```bash
pip install ImgVisFeat
```

### Verify Installation

Verify that ImgVisFeat is installed correctly:

```python
import imvf
print(imvf.__version__)
```

## Quick Start

### Using the All-in-One Visualizer

The simplest way to use ImgVisFeat is with the `Visualizer` class, which applies all visualization methods:

```python
import imvf

# Create visualizer instance
visualizer = imvf.Visualizer()

# Visualize all features and save results
visualizer.visualize("path/to/image.jpg")
```

This will:

1. Display all visualizations in OpenCV windows
1. Save the results to a directory named after the image (e.g., `path/to/image/`)

### Using Individual Visualizers

For more control, use individual visualizers:

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Color channel visualization
color_visualizer = imvf.ColorChannelVisualizer()
result = color_visualizer(image)

# Access individual channels
cv2.imshow("Blue Channel", result.blue)
cv2.imshow("Green Channel", result.green)
cv2.imshow("Red Channel", result.red)
cv2.waitKey(0)
```

### Using the Command Line Interface

ImgVisFeat provides a CLI for quick visualizations:

```bash
# Visualize all features
imvf path/to/image.jpg

# Visualize specific method
imvf path/to/image.jpg --method hog
```

Available methods:

- `all` - All visualization methods (default)
- `color_channel` - RGB channel visualization
- `gradient` - Gradient visualization
- `hog` - Histogram of Oriented Gradients
- `lbp` - Local Binary Patterns
- `keypoint` - Keypoint detection (SIFT, AKAZE, ORB)
- `power_spectrum` - Power spectrum analysis

## Next Steps

- Explore the [User Guide](guide/index.md) for detailed usage of each visualizer
- Check the [CLI Reference](cli.md) for command-line options
- Browse the [API Reference](api/index.md) for complete documentation

## Troubleshooting

### Import Error

If you encounter import errors, ensure that:

1. ImgVisFeat is installed in your current environment
1. You're using Python >= 3.10
1. All dependencies are installed

### OpenCV Display Issues

If images don't display:

1. Ensure you have a GUI backend available
1. Add `cv2.waitKey(0)` after `cv2.imshow()` calls
1. Use `cv2.destroyAllWindows()` to close all windows

### Getting Help

If you encounter issues:

1. Check the [documentation](https://chatflip.github.io/ImgVisFeat/)
1. Search existing [GitHub issues](https://github.com/chatflip/ImgVisFeat/issues)
1. Open a new issue with details about your problem

# ImgVisFeat

**Image Visualization and Feature Extraction Library**

ImgVisFeat is a Python library for image visualization and feature extraction, providing a comprehensive set of tools for analyzing and visualizing various image features.

## Features

ImgVisFeat provides the following visualization and feature extraction capabilities:

### Color Channel Visualization

Extract and visualize individual RGB color channels to analyze color distribution in images.

### Gradient Visualization

Compute and visualize image gradients in X, Y, and combined XY directions:

- **ColorGradientVisualizer**: For color images
- **GrayGradientVisualizer**: For grayscale images

### HoG (Histogram of Oriented Gradients)

Visualize feature descriptors commonly used for object detection and recognition.

### LBP (Local Binary Patterns)

Extract texture descriptors for texture classification and analysis.

### Keypoint Detection

Detect and visualize keypoints using multiple algorithms:

- SIFT (Scale-Invariant Feature Transform)
- AKAZE (Accelerated-KAZE)
- ORB (Oriented FAST and Rotated BRIEF)

### Power Spectrum Analysis

Analyze frequency domain characteristics of images using Fourier Transform.

### CLI Tool

Command-line interface for quick visualizations without writing code.

## Quick Start

### Installation

```bash
pip install ImgVisFeat
```

### Basic Usage

=== "All-in-One Visualizer"

````
```python
import imvf

# Create visualizer instance
visualizer = imvf.Visualizer()

# Visualize all features and save results
visualizer.visualize("path/to/image.jpg")
```
````

=== "Individual Visualizers"

````
```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Color channel visualization
color_channel = imvf.ColorChannelVisualizer()
result = color_channel(image)
cv2.imshow("Blue Channel", result.blue)
cv2.imshow("Green Channel", result.green)
cv2.imshow("Red Channel", result.red)

# HoG visualization
hog = imvf.HoGVisualizer()
result = hog(image)
cv2.imshow("HoG", result.hog)
```
````

=== "Command Line"

````
```bash
# Visualize all features
imvf path/to/image.jpg

# Visualize specific feature
imvf path/to/image.jpg --method hog
```
````

## Documentation

- [Getting Started](getting-started.md) - Installation and basic usage
- [User Guide](guide/index.md) - Detailed guides for each visualizer
- [CLI Reference](cli.md) - Command-line interface documentation
- [API Reference](api/index.md) - Complete API documentation

## Requirements

- Python >= 3.10
- NumPy
- OpenCV
- scikit-image
- Pydantic >= 2.0.0

## Project Status

ImgVisFeat is a personal project created for learning and experimentation. While it's open-source and you're welcome to use and learn from it, please note that it may not be actively maintained or updated regularly.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/chatflip/ImgVisFeat/blob/main/LICENSE) file for details.

## Links

- [GitHub Repository](https://github.com/chatflip/ImgVisFeat)
- [PyPI Package](https://pypi.org/project/ImgVisFeat/)
- [Issue Tracker](https://github.com/chatflip/ImgVisFeat/issues)

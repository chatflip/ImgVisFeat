# All-in-One Visualizer

The `Visualizer` class provides a convenient way to apply all visualization methods at once.

## Usage

```python
import imvf

# Create visualizer instance
visualizer = imvf.Visualizer()

# Visualize all features
visualizer.visualize("path/to/image.jpg")
```

## What It Does

The `Visualizer` class:

1. Loads the image from the specified path
1. Applies all available visualizers:
   - Color Channel Visualization
   - Gradient Visualization (both color and grayscale)
   - HoG Features
   - LBP Features
   - Keypoint Detection (SIFT, AKAZE, ORB)
   - Power Spectrum
1. Displays all results in OpenCV windows
1. Saves all results to a directory named after the image

## Output Directory

Results are saved to a directory structure:

```
path/to/image/
├── color_channels/
│   ├── blue.png
│   ├── green.png
│   └── red.png
├── gradients/
│   ├── gradient_x.png
│   ├── gradient_y.png
│   └── gradient_xy.png
├── hog/
│   └── hog.png
├── lbp/
│   └── lbp.png
├── keypoints/
│   ├── sift.png
│   ├── akaze.png
│   └── orb.png
└── power_spectrum/
    └── power_spectrum.png
```

## Advanced Usage

### Using with Pre-loaded Images

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.Visualizer()

# Process the loaded image
# (Note: visualize() expects a path, use individual visualizers for pre-loaded images)
```

### Accessing Individual Visualizers

The `Visualizer` class internally uses individual visualizers. For more control, use them directly:

```python
import cv2
import imvf

image = cv2.imread("path/to/image.jpg")

# Use individual visualizers
color_viz = imvf.ColorChannelVisualizer()
hog_viz = imvf.HoGVisualizer()

color_result = color_viz(image)
hog_result = hog_viz(image)
```

## See Also

- [Individual Visualizers](index.md) - Detailed guides for each visualizer
- [API Reference](../api/visualizers.md#base-visualizer) - Complete API documentation

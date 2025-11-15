# User Guide

This guide provides detailed information on using each visualizer in ImgVisFeat.

## Available Visualizers

ImgVisFeat provides several specialized visualizers for different types of image analysis:

### Feature Extraction

- [Color Channels](color-channels.md) - Extract and visualize RGB color channels
- [Gradients](gradients.md) - Compute and visualize image gradients
- [HoG Features](hog.md) - Histogram of Oriented Gradients for object detection
- [LBP Features](lbp.md) - Local Binary Patterns for texture analysis
- [Keypoint Detection](keypoints.md) - Detect and visualize keypoints (SIFT, AKAZE, ORB)
- [Power Spectrum](power-spectrum.md) - Frequency domain analysis

### All-in-One

- [Visualizer Class](visualizer.md) - Apply all visualizations at once

## Common Usage Pattern

All individual visualizers follow the same usage pattern:

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.SomeVisualizer()

# Apply visualization
result = visualizer(image)

# Access results
# Results are dataclass instances with specific fields
```

## Result Types

Each visualizer returns a typed result object containing the visualization results:

- `ColorChannelResult` - Blue, Green, Red channels
- `GradientResult` - Gradient X, Y, XY
- `HogResult` - HoG visualization
- `LBPResult` - LBP visualization
- `KeypointResult` - Keypoint and rich keypoint images
- `PowerSpectrumResult` - Power spectrum visualization

See the [API Reference](../api/results.md) for complete details on each result type.

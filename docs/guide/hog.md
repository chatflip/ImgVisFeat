# HoG (Histogram of Oriented Gradients)

Visualize HoG feature descriptors commonly used for object detection and recognition.

## Usage

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.HoGVisualizer()

# Apply visualization
result = visualizer(image)

# Display result
cv2.imshow("HoG Features", result.hog)
cv2.waitKey(0)
```

## Result Structure

The `HogResult` dataclass contains:

- `hog`: HoG feature visualization

## What is HoG?

HoG (Histogram of Oriented Gradients) is a feature descriptor used in computer vision for object detection. It:

- Divides the image into small cells
- Computes gradient histograms for each cell
- Normalizes across blocks of cells
- Creates a feature vector describing the image

## Use Cases

- Object detection (pedestrians, vehicles, etc.)
- Shape recognition
- Image classification
- Feature extraction for machine learning

## See Also

- [API Reference](../api/visualizers.md#hog-visualizer) - Complete API documentation
- [HogResult](../api/results.md#hogresult) - Result type details
- [scikit-image HoG documentation](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_hog.html)

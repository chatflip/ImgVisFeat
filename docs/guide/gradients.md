# Gradient Visualization

Compute and visualize image gradients in X, Y, and combined XY directions.

## Visualizers

ImgVisFeat provides two gradient visualizers:

### ColorGradientVisualizer

For color (RGB) images.

```python
import cv2
import imvf

# Load color image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.ColorGradientVisualizer()

# Apply visualization
result = visualizer(image)

# Display results
cv2.imshow("Gradient X", result.gradient_x)
cv2.imshow("Gradient Y", result.gradient_y)
cv2.imshow("Gradient XY", result.gradient_xy)
cv2.waitKey(0)
```

### GrayGradientVisualizer

For grayscale images.

```python
import cv2
import imvf

# Load and convert to grayscale
image = cv2.imread("path/to/image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create visualizer
visualizer = imvf.GrayGradientVisualizer()

# Apply visualization
result = visualizer(gray)

# Display results
cv2.imshow("Gradient X", result.gradient_x)
cv2.imshow("Gradient Y", result.gradient_y)
cv2.imshow("Gradient XY", result.gradient_xy)
cv2.waitKey(0)
```

## Result Structure

The `GradientResult` dataclass contains:

- `gradient_x`: Gradient in X direction (horizontal)
- `gradient_y`: Gradient in Y direction (vertical)
- `gradient_xy`: Combined gradient magnitude

## Use Cases

- Edge detection
- Feature extraction for object recognition
- Image analysis and preprocessing
- Understanding directional changes in images

## See Also

- [API Reference](../api/visualizers.md#gradient-visualizers) - Complete API documentation
- [GradientResult](../api/results.md#gradientresult) - Result type details

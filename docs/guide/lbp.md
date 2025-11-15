# LBP (Local Binary Patterns)

Extract LBP texture descriptors for texture classification and analysis.

## Usage

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.LBPVisualizer()

# Apply visualization
result = visualizer(image)

# Display result
cv2.imshow("LBP Features", result.lbp)
cv2.waitKey(0)
```

## Result Structure

The `LBPResult` dataclass contains:

- `lbp`: LBP feature visualization

## What is LBP?

LBP (Local Binary Patterns) is a texture descriptor that:

- Compares each pixel with its neighbors
- Creates a binary pattern from the comparisons
- Generates a code describing local texture
- Is rotation and illumination invariant

## Use Cases

- Texture classification
- Face recognition
- Surface inspection
- Material identification
- Medical image analysis

## See Also

- [API Reference](../api/visualizers.md#lbp-visualizer) - Complete API documentation
- [LBPResult](../api/results.md#lbpresult) - Result type details
- [scikit-image LBP documentation](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_local_binary_pattern.html)

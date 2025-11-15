# Color Channel Visualization

Extract and visualize individual RGB color channels from an image.

## Usage

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.ColorChannelVisualizer()

# Apply visualization
result = visualizer(image)

# Display results
cv2.imshow("Blue Channel", result.blue)
cv2.imshow("Green Channel", result.green)
cv2.imshow("Red Channel", result.red)
cv2.waitKey(0)
```

## Result Structure

The `ColorChannelResult` dataclass contains:

- `blue`: Blue channel as grayscale image
- `green`: Green channel as grayscale image
- `red`: Red channel as grayscale image

## Use Cases

- Analyzing color distribution in images
- Identifying dominant color channels
- Preprocessing for color-based feature extraction
- Understanding color composition

## See Also

- [API Reference](../api/visualizers.md#color-channel-visualizer) - Complete API documentation
- [ColorChannelResult](../api/results.md#colorchannelresult) - Result type details

# Power Spectrum Analysis

Analyze frequency domain characteristics of images using Fourier Transform.

## Usage

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer
visualizer = imvf.PowerSpectrumVisualizer()

# Apply visualization
result = visualizer(image)

# Display result
cv2.imshow("Power Spectrum", result.power_spectrum)
cv2.waitKey(0)
```

## Result Structure

The `PowerSpectrumResult` dataclass contains:

- `power_spectrum`: Power spectrum visualization

## What is Power Spectrum?

Power spectrum analysis:

- Converts image to frequency domain using Fourier Transform
- Shows the magnitude of different frequencies
- High frequencies represent edges and details
- Low frequencies represent smooth areas

## Use Cases

- Image quality assessment
- Noise analysis
- Compression analysis
- Pattern recognition
- Texture analysis
- Identifying periodic patterns

## See Also

- [API Reference](../api/visualizers.md#power-spectrum-visualizer) - Complete API documentation
- [PowerSpectrumResult](../api/results.md#powerspectrumresult) - Result type details
- [Fourier Transform Tutorial](https://docs.opencv.org/4.x/de/dbc/tutorial_py_fourier_transform.html)

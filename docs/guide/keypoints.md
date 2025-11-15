# Keypoint Detection

Detect and visualize keypoints using SIFT, AKAZE, or ORB algorithms.

## Usage

```python
import cv2
import imvf

# Load image
image = cv2.imread("path/to/image.jpg")

# Create visualizer with specific algorithm
visualizer = imvf.KeypointVisualizer(algorithm="SIFT")

# Apply visualization
result = visualizer(image)

# Display results
cv2.imshow("Keypoints", result.keypoint)
cv2.imshow("Rich Keypoints", result.rich_keypoint)
cv2.waitKey(0)
```

## Available Algorithms

### SIFT (Scale-Invariant Feature Transform)

```python
visualizer = imvf.KeypointVisualizer(algorithm="SIFT")
```

- Scale and rotation invariant
- High quality features
- Patented (free for research)

### AKAZE (Accelerated-KAZE)

```python
visualizer = imvf.KeypointVisualizer(algorithm="AKAZE")
```

- Fast and efficient
- Scale and rotation invariant
- Open source

### ORB (Oriented FAST and Rotated BRIEF)

```python
visualizer = imvf.KeypointVisualizer(algorithm="ORB")
```

- Very fast
- Rotation invariant
- Free and open source

## Result Structure

The `KeypointResult` dataclass contains:

- `keypoint`: Basic keypoint visualization
- `rich_keypoint`: Detailed keypoint visualization with size and orientation

## Use Cases

- Image matching and alignment
- Object recognition
- 3D reconstruction
- Camera tracking
- Panorama stitching

## See Also

- [API Reference](../api/visualizers.md#keypoint-visualizer) - Complete API documentation
- [KeypointResult](../api/results.md#keypointresult) - Result type details
- [OpenCV Feature Detection](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html)

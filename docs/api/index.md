# API Reference

Complete API documentation for ImgVisFeat.

## Overview

ImgVisFeat follows a consistent design pattern:

1. All visualizers inherit from `AbstractVisualizer`
1. Each visualizer implements a `__call__` method
1. Visualizers return typed dataclass results
1. Results contain visualization images as NumPy arrays

## Quick Reference

### Individual Visualizers

| Visualizer                | Input           | Output                | Use Case                      |
| ------------------------- | --------------- | --------------------- | ----------------------------- |
| `ColorChannelVisualizer`  | RGB image       | `ColorChannelResult`  | Color channel extraction      |
| `ColorGradientVisualizer` | RGB image       | `GradientResult`      | Gradient for color images     |
| `GrayGradientVisualizer`  | Grayscale image | `GradientResult`      | Gradient for grayscale images |
| `HoGVisualizer`           | Any image       | `HogResult`           | Object detection features     |
| `LBPVisualizer`           | Any image       | `LBPResult`           | Texture features              |
| `KeypointVisualizer`      | Any image       | `KeypointResult`      | Keypoint detection            |
| `PowerSpectrumVisualizer` | Any image       | `PowerSpectrumResult` | Frequency analysis            |

## Detailed Documentation

- [Visualizers](visualizers.md) - Complete visualizer class documentation
- [Result Types](results.md) - Result type documentation

## Type Hints

All functions and methods include full type hints for better IDE support:

```python
from numpy.typing import NDArray
import numpy as np

def process_image(image: NDArray[np.uint8]) -> ColorChannelResult:
    ...
```

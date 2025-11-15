# Command Line Interface

ImgVisFeat provides a command-line interface (CLI) for easy access to its visualization features.

## Basic Usage

```bash
ivf [OPTIONS] IMAGE_PATH
```

## Arguments

**IMAGE_PATH**
Path to the input image (required).

## Options

**--method METHOD**
Visualization method to use. Available methods: all, color_channel, gradient, hog, keypoint, lbp, power_spectrum. Default: all

## Examples

1. Visualize using all methods (default):

   ```bash
   ivf input_image.jpg
   ```

1. Visualize using a specific method:

   ```bash
   ivf input_image.jpg --method hog
   ```

1. Visualize using color channel method:

   ```bash
   ivf input_image.jpg --method color_channel
   ```

## Implementation Details

The CLI is implemented in the `imvf.cli` module.

::: imvf.cli.main

## Error Handling

If an error occurs during the visualization process, an error message will be printed to stderr.

## Notes

- The visualizer will automatically display the result unless otherwise specified.
- The 'all' method option will run all available visualization methods on the input image.

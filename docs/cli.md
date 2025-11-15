# Command Line Interface

ImgVisFeat provides a command-line interface (CLI) built with [Typer](https://typer.tiangolo.com/) for easy access to its visualization features.

## Basic Usage

```bash
imvf [COMMAND] IMAGE_PATH
```

The CLI uses subcommands for different visualization methods, making it intuitive and easy to use.

## Getting Help

```bash
# Show main help with all available commands
imvf --help

# Show help for a specific command
imvf all --help
imvf hog --help
```

## Available Commands

### `all` - Visualize All Features

Applies all visualization methods to the input image.

```bash
imvf all path/to/image.jpg
```

### `color-channel` - Color Channel Visualization

Extracts and visualizes individual RGB color channels.

```bash
imvf color-channel path/to/image.jpg
```

### `gradient` - Gradient Visualization

Computes and visualizes image gradients in X, Y, and combined XY directions.

```bash
imvf gradient path/to/image.jpg
```

### `hog` - Histogram of Oriented Gradients

Visualizes HoG feature descriptors for object detection.

```bash
imvf hog path/to/image.jpg
```

### `keypoint` - Keypoint Detection

Detects and visualizes keypoints using SIFT, AKAZE, and ORB algorithms.

```bash
imvf keypoint path/to/image.jpg
```

### `lbp` - Local Binary Patterns

Extracts and visualizes LBP texture descriptors.

```bash
imvf lbp path/to/image.jpg
```

### `power-spectrum` - Power Spectrum Analysis

Analyzes and visualizes frequency domain characteristics.

```bash
imvf power-spectrum path/to/image.jpg
```

## Examples

### Basic Examples

```bash
# Visualize all features
imvf all input_image.jpg

# Visualize only HoG features
imvf hog input_image.jpg

# Visualize keypoints
imvf keypoint input_image.jpg

# Visualize color channels
imvf color-channel input_image.jpg
```

### Using with Different Image Formats

```bash
# Works with various image formats
imvf all image.jpg
imvf gradient image.png
imvf hog image.bmp
```

## Features

### Built with Typer

The CLI is built with Typer, providing:

- **Beautiful help messages** with formatted output
- **Shell completion** support (install with `imvf --install-completion`)
- **Type-safe arguments** with automatic validation
- **Intuitive subcommand structure**

### Auto-completion

Install shell completion for enhanced productivity:

```bash
# Install completion for your shell
imvf --install-completion

# Show completion script
imvf --show-completion
```

## Implementation Details

The CLI is implemented in the `imvf.cli` module using the Typer framework.

::: imvf.cli.app
    options:
      show_root_heading: true
      show_source: false

## Error Handling

If an error occurs during the visualization process:

- Error messages are printed to stderr
- The command exits with code 1
- A helpful error message indicates what went wrong

Example error output:

```bash
$ imvf all nonexistent.jpg
Error: Image not found: nonexistent.jpg
Visualization failed.
```

## Output

All visualization methods:

- Display results in OpenCV windows
- Save results to a directory named after the input image
- Print progress information to stdout

Example output:

```bash
$ imvf all sample.jpg
Visualizing sample.jpg
Number of keypoints (SIFT) : 957
Number of keypoints (AKAZE): 513
Number of keypoints (ORB): 500
Visualization complete.
```

## Notes

- Each subcommand represents a specific visualization method
- The `all` command runs all available visualization methods
- Results are automatically saved to an output directory
- Press any key in the OpenCV window to close the visualization

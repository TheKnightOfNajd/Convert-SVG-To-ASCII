# SVG to ASCII Art Converter

## Overview

This script converts an **SVG** image into **ASCII art** by:

1. Converting the SVG to PNG using **CairoSVG**.
2. Processing the PNG image with **Pillow (PIL)** and **NumPy**.
3. Applying a threshold to determine dark and light areas.
4. Resizing the image for better ASCII representation.
5. Generating ASCII output and saving it to a text file.

## Requirements

Ensure you have the following Python packages installed:

```bash
pip install -r requirements.txt
```

## Usage

Run the script and provide the path to an **SVG** file:

```python
convert_svg_to_ascii("Saudi_Riyal_Symbol.svg", scale_percent=100, skip_factor=1)
```

### Parameters:

- **svg\_path** (str): Path to the input SVG file.
- **output\_txt** (str, default="ascii\_art.txt"): Path for saving the ASCII output.
- **scale\_percent** (int, default=30): Controls the scaling of the image for better detail.
- **skip\_factor** (int, default=5): Adjusts the density of ASCII characters (lower values retain more details).

### Output

The resulting ASCII art is saved in the specified text file.

##

## Notes

- Modify `threshold`, `scale_percent`, and `skip_factor` to fine-tune the ASCII output.
- The script supports transparency detection to maintain the shape of the image.

## License

MIT License

---

**Author:** TheKnightOfNajd\
**Version:** 1.0


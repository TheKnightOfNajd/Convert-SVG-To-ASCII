from PIL import Image
import numpy as np
import cairosvg

def convert_svg_to_ascii(svg_path, output_txt="ascii_art.txt", scale_percent=30, skip_factor=5):
    # Convert SVG to PNG
    png_path = svg_path.replace(".svg", ".png")
    cairosvg.svg2png(url=svg_path, write_to=png_path)

    # Load the PNG image with transparency support
    img = Image.open(png_path).convert("RGBA")

    # Convert image to NumPy array
    img_array = np.array(img)

    # Extract the alpha channel (for transparency detection)
    alpha_channel = img_array[:, :, 3]

    # Convert to grayscale for thresholding
    gray_img = np.mean(img_array[:, :, :3], axis=2)

    # Create a binary mask: Black (dark) areas -> 1, Light (bright) areas -> 0
    threshold = 128  # Adjust if needed
    binary_img = np.where((gray_img < threshold) & (alpha_channel > 0), 1, 0)
    
    original_height, original_width = binary_img.shape
    # Resize to a larger scale for more detail
    height, width = binary_img.shape
    aspect_ratio = original_width / original_height
    new_width = int(width * scale_percent *2 / 100)
    height_adjustment_factor = 3  # Increase to shorten height (e.g., 1.5, 2.0)
    new_height = int(new_width / aspect_ratio / height_adjustment_factor)

    # Resize using nearest-neighbor interpolation to maintain clarity
    binary_img_resized = np.array(Image.fromarray(binary_img.astype(np.uint8) * 255)
                                  .resize((new_width, new_height), Image.NEAREST)) // 255

    # Convert binary image to ASCII text with reduced skipping
    ascii_art = "\n".join([
        "".join('1' if binary_img_resized[i, j] == 1 else '0'
                for j in range(0, binary_img_resized.shape[1], skip_factor))
        for i in range(0, binary_img_resized.shape[0], skip_factor)
    ])

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(ascii_art)

    print(f"✅ ASCII Art saved to {output_txt}")

convert_svg_to_ascii("Saudi_Riyal_Symbol.svg", scale_percent=100, skip_factor=1)

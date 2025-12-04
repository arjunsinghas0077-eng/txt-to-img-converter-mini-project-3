import argparse
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import platform

# --- Configuration ---
OUTPUT_DIR = "output_images"

# Common font paths on different operating systems
WINDOWS_FONTS = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    r"C:\Windows\Fonts\verdana.ttf",
]

MAC_FONTS = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]

LINUX_FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

FALLBACK_FONT_PATH = "arial.ttf"  # In case no system font exists


def find_font():
    """Detects the best available font depending on OS."""
    system = platform.system()

    if system == "Windows":
        for f in WINDOWS_FONTS:
            if os.path.exists(f):
                return f

    elif system == "Darwin": 
        for f in MAC_FONTS:
            if os.path.exists(f):
                return f

    elif system == "Linux":
        for f in LINUX_FONTS:
            if os.path.exists(f):
                return f

    # Final fallback
    return FALLBACK_FONT_PATH


def generate_image(prompt: str, output_filename: str, width: int = 800, height: int = 600):
    """Generates a stylized image with wrapped text."""
    try:
        # Creating a base image
        img = Image.new('RGB', (width, height), color=(25, 25, 112))  # Midnight Blue
        d = ImageDraw.Draw(img)

        # Loading the font
        font_path = find_font()
        try:
            font_size = 50
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Warning: Could not load font from {font_path}. Using default PIL font.")
            font = ImageFont.load_default()
            font_size = 16

        # Wrapping the text
        avg_char_width = font_size * 0.6
        max_chars_per_line = int((width * 0.9) / avg_char_width)
        wrapped_text = textwrap.fill(prompt, width=max_chars_per_line)

        # Calculate text position
        bbox = d.textbbox((0, 0), wrapped_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) / 2
        y = (height - text_height) / 2

        # Drawing the text
        d.text((x, y), wrapped_text, fill=(255, 255, 255), font=font, align="center")

        # For Border
        d.rectangle([(10, 10), (width - 10, height - 10)], outline=(255, 215, 0), width=5)

        # Save
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        img.save(output_path)

        print(f"Successfully generated image: {output_path}")

    except Exception as e:
        print(f"Error generating image: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Simple Python text-to-image converter (Windows compatible)."
    )
    parser.add_argument("prompt", type=str, help="Text to convert into an image.")
    parser.add_argument("-o", "--output", type=str, default="output.png",
                        help="Output filename (default: output.png)")
    parser.add_argument("-W", "--width", type=int, default=800,
                        help="Image width (default: 800)")
    parser.add_argument("-H", "--height", type=int, default=600,
                        help="Image height (default: 600)")

    args = parser.parse_args()

    if not args.prompt.strip():
        print("Error: Prompt cannot be empty.")
        parser.print_help()
        return

    generate_image(args.prompt, args.output, args.width, args.height)


if __name__ == "__main__":
    main()

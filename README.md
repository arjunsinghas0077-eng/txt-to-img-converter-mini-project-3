# Simple Text-to-Image Converter (Mini-Project)

This is a simple Python mini-project that converts a text prompt into a stylized image. It is designed to be easily runnable on a macOS machine with Python and VS Code.

**Note:** This project creates an image that *displays* your text prompt in a stylized way. It does not use advanced AI models to generate a complex image *based* on the prompt's content (e.g., "a cat wearing a hat"). This design choice ensures the project is lightweight, easy to set up, and avoids the need for large model downloads or complex dependencies, which aligns with the "mini-project" and "no Git/Xcode" requirements.

## Requirements

*   **Python 3.9.6 (Pre-installed on any OS or easily installed via VS Code)
*   **Pillow** library (Installed via `pip`)

## Installation and Setup (for macOS users)

1.  **Download:** Download the entire project folder (`text-to-image-converter`) to your computer.
2.  **Open in VS Code:** Open the project folder in Visual Studio Code.
3.  **Open Terminal:** In VS Code, open a new Terminal (`Terminal` -> `New Terminal`).
4.  **Install Dependencies:** Run the following command in the terminal to install the required library:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

Run the script from the terminal, providing your text prompt in quotes:

```bash
python3 main.py "Your text prompt goes here"
```

### Example

```bash
python3 main.py "Hello, this is my first text-to-image conversion using Python!" -o my_creation.png
```

### Optional Arguments

| Argument | Description | Default |
| :--- | :--- | :--- |
| `prompt` | **Required.** The text you want to display in the image. | N/A |
| `-o`, `--output` | The filename for the generated image. | `output.png` |
| `-W`, `--width` | The width of the output image in pixels. | `800` |
| `-H`, `--height` | The height of the output image in pixels. | `600` |

## Output

The generated image will be saved in a folder named `output_images` within the project directory.

## Project Structure

```
text-to-image-converter/
├── main.py             # The core Python script
├── requirements.txt    # List of required Python packages
└── README.md           # This file
```

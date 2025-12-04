Simple Text-to-Image Converter (Mini-Project)

This is a simple Python mini-project that converts a text prompt into a stylized image. It is designed to run easily on Windows, macOS, Linux, and Android with Python installed.

Note: This project creates an image that displays your text prompt in a stylized way.
It does not use advanced AI models to generate images based on the meaning of the prompt (e.g., “a dragon flying over a city”).
This keeps the project lightweight, easy to set up, and perfect for a mini-project.

Requirements

Python 3.x (Works on Windows/macOS/Linux/Android)

Pillow library (Install using pip)

Installation and Setup (for Windows users)

Download: Download the entire project folder (text-to-image-converter) to your computer.

Open in VS Code: Open the project folder in Visual Studio Code.

Open Terminal: In VS Code, open a new Terminal (Terminal → New Terminal).

Install Dependencies: Run the following command:

pip install -r requirements.txt

Android note

If running on Android (Pydroid/Termux), place a .ttf font file (e.g., arial.ttf) next to main.py.

Usage

Run the script from the terminal/command prompt, providing your text prompt in quotes:

python main.py "Your text prompt goes here"

Example
python main.py "Hello, this is my first text-to-image conversion using Python!" -o my_creation.png

Optional Arguments
Argument	Description	Default
prompt	Required. The text you want to display in the image.	N/A
-o, --output	The filename for the generated image.	output.png
-W, --width	The width of the output image in pixels.	800
-H, --height	The height of the output image in pixels.	600
Output

The generated image will be saved in a folder named output_images inside the project directory.

Project Structure
text-to-image-converter/
├── main.py             # The core Python script
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation

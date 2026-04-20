Simple Text-to-Image Converter (Mini-Project)

This is a simple boof Python mini-project that converts a text prompt into a stylized image. It is designed to run easily on Windows, macOS, Linux, and Android with Python installed.

Note: This project creates an image that displays your text prompt in a stylized way.
It does not use advanced AI models to generate images based on the meaning of the prompt. i dont have the time of the resources currently lol.
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


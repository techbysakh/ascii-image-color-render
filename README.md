# ASCII Image Color Renderer 🎨🖼️

A fun and visually appealing Python script that converts images into colored ASCII art with a smooth slow-motion effect in the terminal. Great for artistic console visuals and experimenting with pixel-to-text transformation!

## Features
- 🎨 Converts images into colored ASCII art using true RGB terminal color codes
- 🖼️ Supports any local image file (JPG, PNG, etc.)
- 🌈 Real-time slow-motion rendering line by line
- ✨ Contrast enhancement option for sharper visuals
- 💾 Saves plain ASCII output to a file

## How It Works
The script:
1. Takes a user-provided image path and output filename.
2. Resizes the image based on terminal-friendly dimensions.
3. Enhances the image contrast (optional).
4. Converts pixels to corresponding ASCII characters based on brightness.
5. Renders it live in the terminal, with colored output.
6. Writes the plain ASCII version to a file.

## Usage
```bash
python ascii_render.py

When prompted:

    Enter the path to your image (e.g., photo.jpg)

    Enter your desired output filename (e.g., ascii_output.txt)

# Requirements

    Python 3.6+

    Pillow library

💡 Tip: Best viewed on terminals that support RGB ANSI codes (like most modern Linux/macOS terminals or Windows Terminal).


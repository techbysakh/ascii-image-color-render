from PIL import Image, ImageEnhance
import os
import time

# === CONFIG ===
ASCII_WIDTH = 80
USE_CONTRAST = True
CONTRAST_FACTOR = 1.8
DRAW_DELAY = 0.015 

# ASCII characters from light to dark
ascii_chars = list(" .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")

# Ask for image path and output file name
IMAGE_PATH = input("Enter the path to the image: ")
OUTPUT_FILE = input("Enter the output file name (e.g., ascii_output.txt): ")

# Load image
image = Image.open(IMAGE_PATH)

# Resize with aspect ratio correction
aspect_ratio = image.height / image.width
ascii_height = int(ASCII_WIDTH * aspect_ratio * 0.55)
image = image.resize((ASCII_WIDTH, ascii_height))

# Enhance contrast
if USE_CONTRAST:
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(CONTRAST_FACTOR)

# Convert to RGB
image = image.convert('RGB')
pixels = list(image.getdata())

colored_ascii_lines = []
plain_ascii_lines = []

# Convert image to ASCII line by line
for i in range(0, len(pixels), ASCII_WIDTH):
    line_pixels = pixels[i:i + ASCII_WIDTH]
    colored_line = ""
    plain_line = ""
    
    for r, g, b in line_pixels:
        brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
        char = ascii_chars[brightness * len(ascii_chars) // 256]
        colored_line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        plain_line += char

    colored_ascii_lines.append(colored_line)
    plain_ascii_lines.append(plain_line)

# Clear terminal before drawing
os.system('cls' if os.name == 'nt' else 'clear')

# Draw in slow-motion 🎨✨
for line in colored_ascii_lines:
    print(line)
    time.sleep(DRAW_DELAY)

# Save plain ASCII to file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(plain_ascii_lines))

print(f"\n✅ Slow-motion draw complete. Saved to '{OUTPUT_FILE}'")

import numpy as np
import argparse
import sys
import os

def load_pgm(filename):
    """Load a .pgm image file into a NumPy array"""
    with open(filename, 'rb') as f:
        magic_number = f.readline().strip()
        if magic_number != b'P5':
            raise ValueError("Only binary PGM (P5) format is supported.")

        # Skip comment lines
        while True:
            line = f.readline()
            if line[0] != ord('#'):
                break

        width, height = [int(i) for i in line.strip().split()]
        maxval = int(f.readline().strip())

        # Read image data
        dtype = np.uint8 if maxval < 256 else np.uint16
        img = np.fromfile(f, dtype=dtype).reshape((height, width))
        return img

def save_pgm(filename, img):
    """Save a NumPy array as a .pgm image"""
    height, width = img.shape
    maxval = 255
    with open(filename, 'wb') as f:
        f.write(b'P5\n')
        f.write(f'{width} {height}\n'.encode())
        f.write(f'{maxval}\n'.encode())
        img.astype(np.uint8).tofile(f)

def print_stats(img):
    """Print image statistics"""
    print("\n📊 Image Statistics")
    print(f"Dimensions: {img.shape[1]} x {img.shape[0]}")
    print(f"Mean brightness: {img.mean():.2f}")
    print(f"Standard deviation: {img.std():.2f}")
    print(f"Min pixel: {img.min()}")
    print(f"Max pixel: {img.max()}")

def invert(img):
    return 255 - img

def threshold(img, thresh_val=128):
    return np.where(img >= thresh_val, 255, 0).astype(np.uint8)

def contrast_stretch(img):
    min_val = img.min()
    max_val = img.max()
    if max_val == min_val:
        return np.zeros_like(img)
    stretched = (img - min_val) * (255.0 / (max_val - min_val))
    return stretched.astype(np.uint8)
def image_to_ascii(image, width=80):
    ASCII_CHARS = "@%#*+=-:. "
    height, original_width = image.shape
    aspect_ratio = height / original_width
    new_height = int(aspect_ratio * width * 0.55)

    x_step = max(1, original_width // width)
    y_step = max(1, height // new_height)
    resized = image[::y_step, ::x_step]

    ascii_art = ""
    for row in resized:
        for pixel in row:
            ascii_art += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
        ascii_art += "\n"
    return ascii_art

def main():
    parser = argparse.ArgumentParser(description="🖼️ CLI Image Processor (Grayscale .pgm only)")
    parser.add_argument("input", help="Input .pgm image")
    parser.add_argument("output", help="Output .pgm image")
    parser.add_argument("--invert", action="store_true", help="Apply inversion")
    parser.add_argument("--threshold", type=int, help="Apply thresholding at value (0-255)")
    parser.add_argument("--contrast", action="store_true", help="Apply contrast stretching")
    parser.add_argument("--stats", action="store_true", help="Show image statistics")
    parser.add_argument("--ascii", action="store_true", help="Show ASCII preview before and after processing")

    args = parser.parse_args()

    # Debug info
    print(f"\n📂 Loading image: {args.input}")
    if not os.path.exists(args.input):
        print("❌ File does not exist.")
        sys.exit(1)

    try:
        img = load_pgm(args.input)
        print("✅ Image loaded successfully.")
    except Exception as e:
        print(f"❌ Failed to load image: {e}")
        sys.exit(1)

    original_img = img.copy()

    if args.ascii:
        print("\n🖼️  Original Image Preview (ASCII):")
        print(image_to_ascii(original_img))

    if args.stats:
        print_stats(img)

    if args.invert:
        img = invert(img)
        print("✅ Inversion applied.")

    if args.threshold is not None:
        img = threshold(img, args.threshold)
        print(f"✅ Thresholding applied at {args.threshold}.")

    if args.contrast:
        img = contrast_stretch(img)
        print("✅ Contrast stretching applied.")

    if args.ascii:
        print("\n🎨 Processed Image Preview (ASCII):")
        print(image_to_ascii(img))

    try:
        save_pgm(args.output, img)
        print(f"💾 Image saved to {args.output}")
    except Exception as e:
        print(f"❌ Failed to save image: {e}")

if __name__ == "__main__":
    main()

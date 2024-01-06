from PIL import Image
import os

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            img.thumbnail(size)
            img.save(output_path)
            print("Image resized and saved successfully!")
    except Exception as e:
        print(f"Error: {e}")

def convert_image_format(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
            print("Image converted and saved successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = "input_image.jpg"
    output_resized_path = "resized_image.jpg"
    output_format_path = "converted_image.png"

    # Size for the resized image (width, height)
    new_size = (300, 300)

    # Resize image
    resize_image(input_image_path, output_resized_path, new_size)

    # Convert image format
    convert_image_format(input_image_path, output_format_path, "PNG")

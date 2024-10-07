import os
from PIL import Image

def convert_jpeg_to_png(input_path):
    try:
        # Start
        print("Starting JPEG to PNG conversion process...")

        # Check if it's a JPEG file
        if not input_path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Not a JPEG file")

        # Load JPEG file
        print("Loading JPEG file...")
        with Image.open(input_path) as img:
            # Convert to PNG
            print("Converting to PNG...")
            output_path = os.path.splitext(input_path)[0] + ".png"
            
            # Save PNG file
            img.save(output_path, "PNG")
            print(f"PNG file saved as: {output_path}")

        # End
        print("Conversion completed successfully!")
        return True

    except Exception as e:
        # Error
        print(f"Error: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    while True:
        input_file = input("Enter the path to your JPEG file (or 'q' to quit): ")
        if input_file.lower() == 'q':
            break
        
        success = convert_jpeg_to_png(input_file)
        if success:
            print("Conversion successful.")
        else:
            print("Conversion failed.")
        print()  # Empty line for readability

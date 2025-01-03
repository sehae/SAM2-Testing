from PIL import Image
import os


def resize_images(input_folder, output_folder, size=(1024, 1024)):
    """Resize all images in the input folder to the specified size and save them to the output folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save resized images.
        size (tuple): Desired size for the resized images (width, height).
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if not os.path.isfile(input_path):
            continue
        try:
            with Image.open(input_path) as img:
                # Resize the image
                img_resized = img.resize(size, Image.LANCZOS)

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)

                print(f"Resized and saved: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")


if __name__ == "__main__":
    input_folder = "./data/train/"
    output_folder = "./resize/"
    resize_images(input_folder, output_folder)

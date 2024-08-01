# image_handler.py
import os
import random

def select_random_image(image_dir):
    # jmf's Image Selector
    # Get a list of all files in the directory
    files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    # Filter out files that are not images (simple filter by extension)
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # Select a random image
    selected_image = random.choice(images) if images else None
    return os.path.join(image_dir, selected_image) if selected_image else None

# Example usage
if __name__ == '__main__':
    image_dir_path = 'path/to/your/image/directory'  # Update this path to your image directory
    selected_image_path = select_random_image(image_dir_path)
    if selected_image_path:
        print(f"Selected Image: {selected_image_path}")
    else:
        print("No images found in the directory.")

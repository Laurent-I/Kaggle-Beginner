import os
import random
import shutil

def move_images_to_test(src_folder, test_folder, percentage=0.5):
    # Create the test folder if it doesn't exist
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    # Get a list of all image files in the src folder
    images = [f for f in os.listdir(src_folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

    # Shuffle the images so that we get a random selection
    random.shuffle(images)

    # Determine how many images to move to the test folder
    num_images = int(len(images) * percentage)

    # Move the selected images to the test folder
    for i in range(num_images):
        src_path = os.path.join(src_folder, images[i])
        dst_path = os.path.join(test_folder, images[i])
        shutil.move(src_path, dst_path)
        print(f"Moving {images[i]} to test folder")

# Example usage:
parent = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\elephant\\test'
child = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\elephant\\test\\valid'
move_images_to_test(parent, child)

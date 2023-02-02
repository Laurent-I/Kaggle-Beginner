
import os

def rename_images(path):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isdir(full_path):
            rename_images(full_path)
        elif filename.endswith(".jpg"):
            new_file_name = filename[:-4] + ".png"
            os.rename(full_path, os.path.join(path, new_file_name))
            print(f"Renaming {filename} from .jpg to .png")

path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data'

rename_images(path)


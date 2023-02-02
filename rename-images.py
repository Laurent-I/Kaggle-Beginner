import os
import random
import string

def rename_images(path):
    for filename in os.listdir(path):
        if (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")):
            new_file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + os.path.splitext(filename)[1]
            os.rename(os.path.join(path, filename), os.path.join(path, new_file_name))
            print(f"Renaming {filename} to {new_file_name}")



path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\elephant'

rename_images(path)
import os

def rename_images(path):
    i = 1676
    for filename in os.listdir(path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            new_file_name = str(i) + filename[filename.rindex("."):]
            os.rename(os.path.join(path, filename), os.path.join(path, new_file_name))
            i += 1
            print(f"Renaming {filename} to {new_file_name}")



path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\rhino'

rename_images(path)
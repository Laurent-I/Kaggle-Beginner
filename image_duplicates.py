import os
import imagehash
from PIL import Image

def detect_duplicate_images(dir1, dir2):
  """
  Detects duplicate images by comparing every image in directory 1 to every other image in directory 2.
    
  Parameters:
  dir1 -- The first directory to search for images
  dir2 -- The second directory to search for images
    
  Returns:
  A list of tuples, where each tuple contains the file path of a duplicate image in both directories.
  """
  # Get a list of all image files in both directories
  images1 = [os.path.join(dir1, f) for f in os.listdir(dir1) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
  images2 = [os.path.join(dir2, f) for f in os.listdir(dir2) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

  # Create a dictionary to store the hashes of all images in directory 1
  hashes = {}
  for image in images1:
    with Image.open(image) as img:
        hash = str(imagehash.phash(img))
        if hash not in hashes:
            hashes[hash] = [image]
        else:
            hashes[hash].append(image)

  # Check for duplicates in directory 2
  duplicates = []
  for image in images2:
    with Image.open(image) as img:
        hash = str(imagehash.phash(img))
        if hash in hashes:
            duplicates.append((image, hashes[hash][0]))
                
  return duplicates


DIR1 = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\valid'
DIR2 = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\train'
duplicates = detect_duplicate_images(DIR1, DIR2)
for duplicate in duplicates:
    print('Duplicate found:', duplicate[0], 'and', duplicate[1])

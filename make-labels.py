import os
import random
import csv
import re

def remove_words_after_dot(string):
    return re.split("\.", string)[0]

csv_file_location =  'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\image_labels.csv'

def get_image_names_and_label(path, label):
    image_names = []
    for filename in os.listdir(path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            filename = remove_words_after_dot(filename)
            image_names.append(filename)
            print(filename)
    
    with open(csv_file_location, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "label"])
        for i, name in enumerate(image_names, 1):
            writer.writerow([name,  label])


path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data\\data\\cheetah'
get_image_names_and_label(path, 'cheetah')

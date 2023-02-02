import os

def delete_files(path):
  for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path) and filename.endswith(".txt"):
      os.remove(file_path)
    elif os.path.isdir(file_path):
      delete_files(file_path)
      print(f"deleting {filename} !!!")

path = 'C:\\Users\\Pc\\Downloads\\Compressed\\data'
delete_files(path)
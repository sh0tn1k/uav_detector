from PIL import Image
import os

def compress_image(input_path, quality=95):
    if os.path.exists(input_path):
      with Image.open(input_path) as img:
          img.save(input_path, quality=quality, optimize=True)
    else:
        print(f"NOT EXIST: {input_path}")

def compress_files_in_directory(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            compress_image(file_path)

# Example of use
directory_path = '/wrk/dataset_v1/plane'
compress_files_in_directory(directory_path)
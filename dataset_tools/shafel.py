import os
import shutil
import random
from sklearn.model_selection import train_test_split

# Paths to folders with images of two classes
class1_path = '/wrk/dataset_v1/no_plane'
class2_path = '/wrk/dataset_v1/plane'

# Target folder paths
train_path = '/wrk/dataset_v1/train'
valid_path = '/wrk/dataset_v1/valid'
test_path = '/wrk/dataset_v1/test'

# Collect all the images
images = []
for class_path in [class1_path, class2_path]:
    for image in os.listdir(class_path):
        images.append((os.path.join(class_path, image), class_path.split('/')[-1]))

# Mixing the images
random.shuffle(images)

# Split into subsets
train_images, test_images = train_test_split(images, test_size=0.3, random_state=42)
valid_images, test_images = train_test_split(test_images, test_size=0.5, random_state=42)

# Function for copying images to the appropriate folders
def copy_images(images, destination):
    for image, class_name in images:
        os.makedirs(os.path.join(destination, class_name), exist_ok=True)
        shutil.copy(image, os.path.join(destination, class_name))

# Copying images
copy_images(train_images, train_path)
copy_images(valid_images, valid_path)
copy_images(test_images, test_path)

def items_in_set(path_of_set):
  for dirpath, dirnames, filenames in os.walk(path_of_set):
    print(f"In '{dirpath}' {len(filenames)} images.")

items_in_set("/wrk/dataset_v1/train")
items_in_set("/wrk/dataset_v1/test")
items_in_set("/wrk/dataset_v1/valid")
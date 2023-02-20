import cv2
import os

base_folder = "/home/stephan/Downloads/walls"
images = os.listdir(base_folder)
print(images)
for image_path in images:
    image = cv2.imread(f"{base_folder}/{image_path}") # Flip horizontal/mirror
    image = cv2.flip(image, 1)
    cv2.imwrite(f"{base_folder}/{image_path}", image)

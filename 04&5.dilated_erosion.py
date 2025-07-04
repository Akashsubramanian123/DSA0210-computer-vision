import cv2
import numpy as np
import os

# Get image path from user
image_path = input("Enter the full path of the image: ")

# Check if the file exists
if not os.path.exists(image_path):
    print("Image file not found at the specified path.")
    exit()

# Load the image in grayscale
image = cv2.imread(image_path, 0)

# Threshold to make it binary
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for dilation and erosion
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Apply erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# Display results
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Binary Image', binary)
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Eroded Image', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
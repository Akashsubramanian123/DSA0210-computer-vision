import cv2
import numpy as np
import os

# Get image path from user
image_path = input("Enter the full path of the image: ")

# Check if file exists
if not os.path.exists(image_path):
    print("Image file not found at the specified path.")
    exit()

# Load the image
image = cv2.imread(image_path)

# Get image dimensions
rows, cols, ch = image.shape

# Define 3 points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define where those points should go in the transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation
affine_transformed = cv2.warpAffine(image, matrix, (cols, rows))

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Affine Transformed Image', affine_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

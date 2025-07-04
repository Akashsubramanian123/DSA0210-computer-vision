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

# Get image size
rows, cols = image.shape[:2]

# Define 4 source points (from the original image)
# You can change these according to your image content
pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])

# Define 4 destination points (where the points should map to)
pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

# Compute the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation
perspective_transformed = cv2.warpPerspective(image, matrix, (cols, rows))

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', perspective_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

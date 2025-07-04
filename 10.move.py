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

# Define the translation offsets
tx = 100  # Shift right by 100 pixels (positive x direction)
ty = 50   # Shift down by 50 pixels (positive y direction)

# Create the translation matrix (2x3)
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Get dimensions of the image
rows, cols = image.shape[:2]

# Apply the translation
translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))

# Show original and moved images
cv2.imshow("Original Image", image)
cv2.imshow(f"Moved Image (Right {tx}px, Down {ty}px)", translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

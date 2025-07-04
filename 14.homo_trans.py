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
rows, cols = image.shape[:2]

# Define 4 points in the source image (e.g., corners of a tilted rectangle)
src_pts = np.float32([
    [100, 100],
    [cols - 100, 80],
    [100, rows - 100],
    [cols - 120, rows - 80]
])

# Define the destination points (a perfect rectangle)
dst_pts = np.float32([
    [0, 0],
    [cols, 0],
    [0, rows],
    [cols, rows]
])

# Compute the Homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply the homography transformation
warped_image = cv2.warpPerspective(image, H, (cols, rows))

# Show the result
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformed Image", warped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

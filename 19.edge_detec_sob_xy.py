import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Apply Sobel operator along X and Y axes
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine gradients using magnitude
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert to 8-bit for display
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# Show the images
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X+Y Edge Detection", sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()

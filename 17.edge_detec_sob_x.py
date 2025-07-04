import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Apply Sobel operator along X axis
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Convert result to 8-bit
abs_sobel_x = cv2.convertScaleAbs(sobel_x)

# Show original and edge-detected image
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X Edge Detection", abs_sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()

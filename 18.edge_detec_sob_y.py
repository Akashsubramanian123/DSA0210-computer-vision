import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Apply Sobel operator along Y axis (dx=0, dy=1)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Convert result to 8-bit for display
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

# Show original and Sobel Y output
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Y (Horizontal Edges)", abs_sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()

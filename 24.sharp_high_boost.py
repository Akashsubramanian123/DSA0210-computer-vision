import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale (or work on color if desired)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to create low-pass version
blurred = cv2.GaussianBlur(gray, (5, 5), 1)

# Set high-boost factor (A > 1)
A = 1.8

# Compute the mask (high-frequency components)
mask = cv2.subtract(gray, blurred)

# Apply high-boost filtering: Original + (A - 1) * Mask
high_boost = cv2.addWeighted(gray, 1.0, mask, A - 1, 0)

# Display the results
cv2.imshow("Original Image", gray)
cv2.imshow("High-Frequency Mask", mask)
cv2.imshow(f"High-Boost Sharpened Image (A={A})", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()

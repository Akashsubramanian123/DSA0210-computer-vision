import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 1: Compute gradients using Sobel operators
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 2: Compute gradient magnitude
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert to 8-bit image
gradient_mask = cv2.convertScaleAbs(gradient_magnitude)

# Step 3: Add gradient mask to original image to enhance edges
alpha = 1.5  # Gradient boost factor
sharpened = cv2.addWeighted(gray, 1.0, gradient_mask, alpha, 0)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Mask", gradient_mask)
cv2.imshow("Sharpened Image (Gradient Masking)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

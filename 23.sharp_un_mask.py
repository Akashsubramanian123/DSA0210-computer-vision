import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale (optional: keep color if needed)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Calculate the mask (details)
mask = cv2.subtract(gray, blurred)

# Sharpen by adding the mask back to the original image
alpha = 1.5  # Sharpening intensity
sharpened = cv2.addWeighted(gray, 1.0, mask, alpha, 0)

# Display results
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Unsharp Mask", mask)
cv2.imshow("Sharpened Image (Unsharp Masking)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

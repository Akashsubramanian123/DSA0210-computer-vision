import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale for sharpening
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define Laplacian kernel with negative center
laplacian_kernel = np.array([[0,  1, 0],
                             [1, -4, 1],
                             [0,  1, 0]])

# Apply filter2D to compute Laplacian
laplacian = cv2.filter2D(gray, cv2.CV_64F, laplacian_kernel)

# Convert Laplacian result to 8-bit
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Sharpen the image by subtracting the Laplacian
sharpened = cv2.subtract(gray, laplacian_abs)

# Display results
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Laplacian", laplacian_abs)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

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

# Extended Laplacian kernel with diagonal neighbors
laplacian_kernel_ext = np.array([[1,  1, 1],
                                 [1, -8, 1],
                                 [1,  1, 1]])

# Apply the Laplacian kernel using filter2D
laplacian_ext = cv2.filter2D(gray, cv2.CV_64F, laplacian_kernel_ext)

# Convert result to 8-bit
laplacian_ext_abs = cv2.convertScaleAbs(laplacian_ext)

# Subtract Laplacian from original to sharpen
sharpened = cv2.subtract(gray, laplacian_ext_abs)

# Display results
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Extended Laplacian (with diagonals)", laplacian_ext_abs)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

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

# Laplacian kernel with positive center
laplacian_kernel_pos = np.array([[-1, -1, -1],
                                 [-1,  8, -1],
                                 [-1, -1, -1]])

# Apply Laplacian kernel using filter2D
laplacian_pos = cv2.filter2D(gray, cv2.CV_64F, laplacian_kernel_pos)

# Convert to 8-bit image
laplacian_pos_abs = cv2.convertScaleAbs(laplacian_pos)

# Add the Laplacian result to the original image for sharpening
sharpened = cv2.add(gray, laplacian_pos_abs)

# Display images
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Laplacian (Positive Center)", laplacian_pos_abs)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

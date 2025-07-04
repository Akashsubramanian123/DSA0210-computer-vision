import cv2
import numpy as np

# Load image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to binary (thresholding)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel (structuring element) for dilation
kernel = np.ones((5, 5), np.uint8)

# Apply Dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Display the results
cv2.imshow("Original Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()

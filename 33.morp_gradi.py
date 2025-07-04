import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to binary using thresholding
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply Morphological Gradient
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

# Display the results
cv2.imshow("Original Binary Image", binary)
cv2.imshow("Morphological Gradient (Edges)", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()

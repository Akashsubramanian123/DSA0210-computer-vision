import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Define a structuring element (kernel)
kernel = np.ones((9, 9), np.uint8)

# Apply Black Hat (extracts small dark objects)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display the results
cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Black Hat Result", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()

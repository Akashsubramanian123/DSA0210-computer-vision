import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Define the structuring element (kernel)
kernel = np.ones((9, 9), np.uint8)

# Apply Top Hat (extracts small bright objects)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display the results
cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Top Hat Result", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()

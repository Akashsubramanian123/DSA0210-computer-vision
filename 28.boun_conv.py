import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Define a simple edge-detection kernel (Laplacian-style)
kernel = np.array([[ 0, -1,  0],
                   [-1,  4, -1],
                   [ 0, -1,  0]])

# Apply the convolution filter
edges = cv2.filter2D(image, ddepth=cv2.CV_64F, kernel=kernel)

# Convert to 8-bit for visualization
edges = cv2.convertScaleAbs(edges)

# Show original and edge image
cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Edge / Boundary Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

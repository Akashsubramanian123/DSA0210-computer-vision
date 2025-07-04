import cv2
import os

# Get image path from user
image_path = input("Enter the full path of the image: ")

# Check if file exists
if not os.path.exists(image_path):
    print("Image file not found.")
    exit()

# Load the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Optional: Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 1.4)

# Apply Canny edge detection
# You can tune the thresholds (100, 200) as needed
edges = cv2.Canny(blurred, 100, 200)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

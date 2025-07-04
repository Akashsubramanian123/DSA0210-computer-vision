import cv2
import os

# Get image path from user
image_path = input("Enter the full path of the image: ")

# Check if the file exists
if not os.path.exists(image_path):
    print("Image file not found at the specified path.")
    exit()

# Load the image
image = cv2.imread(image_path)

# Get image dimensions (height, width)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Rotate 90 degrees clockwise
M_clockwise = cv2.getRotationMatrix2D(center, -90, 1.0)  # Negative angle
rotated_clockwise = cv2.warpAffine(image, M_clockwise, (w, h))

# Rotate 90 degrees counter-clockwise
M_counter = cv2.getRotationMatrix2D(center, 90, 1.0)  # Positive angle
rotated_counter = cv2.warpAffine(image, M_counter, (w, h))

# Show all images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Clockwise (90°)", rotated_clockwise)
cv2.imshow("Rotated Counter-Clockwise (90°)", rotated_counter)

cv2.waitKey(0)
cv2.destroyAllWindows()

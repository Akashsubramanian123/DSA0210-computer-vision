import cv2

# Load the image
image = cv2.imread("C:/Users/akash/Downloads/master_vijay.jpg")  # Replace with your image path

if image is None:
    print("Error: Could not read the image.")
    exit()

# Resize to bigger (scale up by 2x)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Resize to smaller (scale down by 0.5x)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display all versions
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image (2x)', bigger)
cv2.imshow('Smaller Image (0.5x)', smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()

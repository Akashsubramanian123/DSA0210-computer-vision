import cv2

# Load the original image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Step 1: Crop a region (e.g., top-left 100x100 block)
cropped_region = image[50:150, 50:150]  # [y1:y2, x1:x2]

# Step 2: Define where to paste (e.g., bottom-right corner)
# Ensure the destination region has the same size as the cropped region
start_y = image.shape[0] - 100
start_x = image.shape[1] - 100
image[start_y:start_y+100, start_x:start_x+100] = cropped_region

# Step 3: Show results
cv2.imshow("Original Image with Cropped Region Pasted", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

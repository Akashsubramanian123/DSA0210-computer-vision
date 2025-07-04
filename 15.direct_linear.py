import numpy as np
import cv2
import os

# Get image path
image_path = input("Enter full image path: ")

if not os.path.exists(image_path):
    print("Image not found.")
    exit()

# Load the image
img = cv2.imread(image_path)
h, w = img.shape[:2]

# Define 4 corresponding points: (source and destination)
# These are sample points, adjust as needed
src_pts = np.array([
    [100, 100],
    [w - 100, 100],
    [100, h - 100],
    [w - 100, h - 100]
], dtype=np.float32)

dst_pts = np.array([
    [0, 0],
    [w, 0],
    [0, h],
    [w, h]
], dtype=np.float32)

# Step 1: Build matrix A for Ah = 0
A = []
for i in range(4):
    x, y = src_pts[i][0], src_pts[i][1]
    u, v = dst_pts[i][0], dst_pts[i][1]
    A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
    A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])

A = np.array(A)

# Step 2: Solve using SVD: Ah = 0
U, S, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)

# Step 3: Normalize H
H = H / H[2, 2]

# Step 4: Apply transformation
warped = cv2.warpPerspective(img, H, (w, h))

# Show original and transformed image
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

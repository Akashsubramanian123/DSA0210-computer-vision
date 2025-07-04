import cv2

# Load images
image = cv2.imread("C:/Users/akash/downloads/man_watch.jpg")           # Scene image
template = cv2.imread("C:/Users/akash/downloads/watch.jpg")      # Watch template

# Check if images are loaded
if image is None or template is None:
    print("Error: Image(s) not found.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Initialize ORB detector
orb = cv2.ORB_create(nfeatures=1000)

# Detect and compute keypoints and descriptors
kp1, des1 = orb.detectAndCompute(gray_template, None)
kp2, des2 = orb.detectAndCompute(gray_image, None)

# Match descriptors using BFMatcher with Hamming distance
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw top matches
result = cv2.drawMatches(template, kp1, image, kp2, matches[:20], None, flags=2)

# Display result
cv2.imshow("Watch Recognition using ORB", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

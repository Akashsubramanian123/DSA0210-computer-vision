import cv2

# Load the image
image = cv2.imread("C:/Users/akash/downloads/two_cric.jpg")

# Check if image loaded successfully
if image is None:
    print("Error: Image not found.")
    exit()

# Make a copy to draw rectangle and extract object
clone = image.copy()
ref_point = []
cropping = False

# Mouse callback function
def shape_selection(event, x, y, flags, param):
    global ref_point, cropping, clone

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False

        # Draw rectangle
        cv2.rectangle(clone, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("Image", clone)

# Set mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", shape_selection)

# Show image and wait for user to draw rectangle
while True:
    cv2.imshow("Image", clone)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):  # Reset
        clone = image.copy()
    elif key == ord("c"):  # Crop and break
        break

cv2.destroyAllWindows()

# Crop the selected area
if len(ref_point) == 2:
    roi = image[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("Cropped Object", roi)
    cv2.imwrite("cropped_object.jpg", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

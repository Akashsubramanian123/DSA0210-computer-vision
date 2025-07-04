import cv2

# Load the image
image = cv2.imread("C:/Users/akash/downloads/master_vijay.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Define the watermark text and position
watermark_text = "© Akash"
position = (image.shape[1] - 200, image.shape[0] - 20)  # Bottom-right corner

# Add the watermark using cv2.putText()
watermarked_image = image.copy()
cv2.putText(
    watermarked_image,
    watermark_text,
    position,
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(0, 0, 0),  # black color
    thickness=4,
    lineType=cv2.LINE_AA
)

# Optional: Add transparency using blend (like a light watermark)
alpha = 0.7  # transparency
output = cv2.addWeighted(image, 1.0, watermarked_image, alpha, 0)

# Display the original and watermarked image
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()

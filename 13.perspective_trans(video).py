import cv2
import numpy as np

# Open webcam (use 0) or a video file path (e.g., 'video.mp4')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open video source")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Finished or error reading frame.")
        break

    rows, cols = frame.shape[:2]

    # Define 4 source points from the original frame
    src_points = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Define 4 destination points (straightened rectangle)
    dst_points = np.float32([
        [0, 0],
        [cols, 0],
        [0, rows],
        [cols, rows]
    ])

    # Compute perspective transform matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply transformation to the frame
    warped_frame = cv2.warpPerspective(frame, matrix, (cols, rows))

    # Show original and transformed frame
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", warped_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

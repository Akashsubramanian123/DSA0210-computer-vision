import cv2

# Path to your video
video_path = "C:/Users/akash/downloads/walking.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Step 1: Read all frames into a list
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Step 2: Play frames in reverse
for frame in reversed(frames):
    cv2.imshow("Video in Reverse", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cv2.destroyAllWindows()

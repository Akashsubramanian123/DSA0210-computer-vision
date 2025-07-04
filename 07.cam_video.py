import cv2
import time

def play_video(speed_label="normal"):
    cap = cv2.VideoCapture(0)  # 0 means default webcam

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    print(f"Press 'q' to quit | Current Mode: {speed_label.upper()}")

    # Define frame delay based on speed
    if speed_label == "slow":
        delay = 60  # higher delay (slower video)
    elif speed_label == "fast":
        delay = 5   # lower delay (faster video)
    else:
        delay = 30  # normal speed

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame. Exiting ...")
            break

        cv2.imshow(f'Webcam - {speed_label.capitalize()} Motion', frame)

        # Wait for key based on speed
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('n'):
            return "normal"
        elif key == ord('s'):
            return "slow"
        elif key == ord('f'):
            return "fast"

    cap.release()
    cv2.destroyAllWindows()

# Main loop to switch between modes
mode = "normal"
while True:
    mode = play_video(mode)
    if mode is None:
        break

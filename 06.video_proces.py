import cv2

def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    paused = False

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break

            text = f"Speed: {speed:.2f}x"
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("Video", frame)
            # cv2.resizeWindow can be skipped unless you're forcing custom dimensions
            # cv2.resizeWindow("Video", frame.shape[1], frame.shape[0])  ← REMOVE or move after imshow

        delay = max(1, int(1000 / (fps * speed)))
        key = cv2.waitKey(delay if not paused else 100) & 0xFF

        if key == 27:  # ESC key
            break
        elif key == ord(' '):  # SPACE
            paused = not paused
        elif key == ord('+') or key == ord('='):
            speed = min(speed * 2, 32.0)
        elif key == ord('-'):
            speed = max(speed / 2, 0.1)

    cap.release()
    cv2.destroyAllWindows()

# Example usage
play_video("C:/Users/akash/downloads/walking.mp4", speed=1.0)
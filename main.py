import cv2

def nothing(x):
    pass

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    cv2.namedWindow('Webcam')

    # Create a trackbar for brightness adjustment
    cv2.createTrackbar('Brightness', 'Webcam', 50, 100, nothing)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Get the current position of the trackbar
        brightness = cv2.getTrackbarPos('Brightness', 'Webcam')

        # Apply the brightness adjustment
        adjusted_frame = cv2.convertScaleAbs(frame, alpha=1, beta=brightness-50)

        # Display the frame
        cv2.imshow('Webcam', adjusted_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite('captured_frame.png', adjusted_frame)
            print("Frame saved as 'captured_frame.png'")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

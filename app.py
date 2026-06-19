import cv2
from ultralytics import YOLO

def main():
    # Load a pre-trained YOLOv8 model (nano version is fast and lightweight)
    model = YOLO("yolov8n.pt")

    # Set up real-time video input using webcam (0 is usually the default built-in camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to exit the application.")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Apply object detection and tracking automatically using ByteTrack/SORT logic built into YOLO
        # persist=True ensures tracking IDs remain consistent across frames
        results = model.track(source=frame, persist=True, tracker="bytetrack.yaml")

        # Visualize the results on the frame (draws bounding boxes, labels, and tracking IDs)
        annotated_frame = results[0].plot()

        # Display the real-time output window
        cv2.imshow("CodeAlpha Task 4: Object Detection & Tracking", annotated_frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
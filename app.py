import cv2
import time
from PIL import Image
import numpy as np

# Camera URL
camera_url = "rtsp://admin:admin@123@10.10.100.82:554/cam/realmonitor?channel=2&subtype=0"
print(f"Attempting to connect to: {camera_url}")

# Open stream
cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    print("Error: Could not connect to camera stream.")
    print("Trying alternative URL format...")
    
    # Try alternative URL format
    camera_url = "rtsp://admin:admin@123@10.10.100.82:554/cam/realmonitor?channel=2&subtype=0"
    print(f"Attempting to connect to: {camera_url}")
    cap = cv2.VideoCapture(camera_url)

    if not cap.isOpened():
        print("Error: Still could not connect. Please check your camera details.")
else:
    print("Connected to camera stream.")

    # Stream for a set duration (60 seconds)
    start_time = time.time()
    duration = 60  # seconds to stream

    while time.time() - start_time < duration:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame")
            break

        # Convert from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to PIL Image to display
        pil_image = Image.fromarray(frame)

        # Display image
        pil_image.show()

        # Control frame rate
        time.sleep(0.1)

    # Release the video capture object
    cap.release()

print("Stream ended")
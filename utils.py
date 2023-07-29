import cv2


def capture_frame_from_rtsp(rtsp_url, output_path):
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    # Check if the stream is opened correctly
    if not cap.isOpened():
        print("Error: Unable to open RTSP stream.")
        return

    # Read a frame from the stream
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Error: Unable to capture frame.")
        cap.release()
        return

    # Save the frame to the specified output path
    success = cv2.imwrite(output_path, frame)
    cap.release()
    return success

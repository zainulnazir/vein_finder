# vein_finder/hardware/camera.py
from picamera2 import Picamera2
import time


def capture_image(output_path="image.jpg", exposure_time=10000):
    """
    Capture an image using the NoIR Camera V2 with specified exposure time.

    Args:
        output_path (str): Path to save the captured image (default: 'image.jpg').
        exposure_time (int): Exposure time in microseconds (default: 10000us = 10ms).
    """
    try:
        # Initialize the camera
        picam2 = Picamera2()

        # Configure the camera for still capture
        config = picam2.create_still_configuration(main={"size": (640, 480)})
        picam2.configure(config)

        # Set exposure time for IR illumination
        picam2.set_controls({"ExposureTime": exposure_time})

        # Start the camera
        picam2.start()
        time.sleep(2)  # Warm-up time for camera to adjust

        # Capture the image
        picam2.capture_file(output_path)

        # Stop the camera
        picam2.stop()

        print(f"Image captured and saved to {output_path}")
    except Exception as e:
        print(f"Error capturing image: {str(e)}")
        raise  # Re-raise exception for debugging in main app
    finally:
        picam2.close()  # Ensure camera is properly shut down

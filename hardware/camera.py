from picamera2 import Picamera2
picam2 = Picamera2()
picam2.set_controls({"ExposureTime": 10000})
picam2.start()
picam2.capture_file("image.jpg")
picam2.stop()

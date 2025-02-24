from flask import Flask, render_template, send_file, request, Response
from hardware.camera import capture_image
from hardware.leds import turn_on, turn_off, setup as setup_leds, cleanup as cleanup_leds
from hardware.servo import setup as setup_servo, point_laser, cleanup as cleanup_servo
from image_processing.vein_detector import process_image, select_best_vein

app = Flask(__name__)

def perform_scan():
    """Execute the full vein finding process."""
    try:
        # Set up and control LEDs
        setup_leds()
        turn_on()
        # Capture image with optimized exposure for IR
        capture_image(exposure_time=10000)  # Adjust exposure as needed
        turn_off()
        cleanup_leds()

        # Process image to detect veins
        contours = process_image('image.jpg')
        point, _ = select_best_vein(contours)

        # Point laser if a vein is found
        if point:
            pwm = setup_servo()
            point_laser(pwm, point[0], 640, 10)  # Adjust image_width and physical_width
            cleanup_servo(pwm)
        
        return "Scan completed successfully"
    except Exception as e:
        return f"Error during scan: {str(e)}"

@app.route('/')
def index():
    """Render the main page with scan button and image display."""
    return render_template('index.html')

@app.route('/image')
def get_image():
    """Serve the processed image."""
    try:
        return send_file('processed_image.jpg', mimetype='image/jpeg')
    except FileNotFoundError:
        return Response("Image not found", status=404)

@app.route('/scan', methods=['POST'])
def scan():
    """Trigger the scan process when the button is pressed."""
    result = perform_scan()
    return Response(result, mimetype='text/plain')

# Note: The app is run from main.py, so no app.run() here

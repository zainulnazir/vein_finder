from hardware.camera import capture_image
from hardware.leds import turn_on, turn_off, setup as setup_leds, cleanup as cleanup_leds
from hardware.servo import setup as setup_servo, point_laser, cleanup as cleanup_servo
from image_processing.vein_detector import process_image, select_best_vein
from web_app.app import app

def perform_scan():
    setup_leds()
    turn_on()
    capture_image(exposure_time=10000)  # Adjust exposure as needed
    turn_off()
    cleanup_leds()
    contours = process_image('image.jpg')
    point, _ = select_best_vein(contours)
    if point:
        pwm = setup_servo()
        point_laser(pwm, point[0], 640, 10)  # Adjust image_width and physical_width
        cleanup_servo(pwm)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
